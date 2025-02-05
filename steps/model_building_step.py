import logging
from typing import Annotated

import mlflow
import pandas as pd
from sklearn.base import RegressorMixin
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from zenml import ArtifactConfig, step
from zenml.client import Client

# Get the active experiment tracker from zenml

experiment_tracker = Client().active_stack.experiment_tracker
from zenml import Model

# model initializtion 
model = Model(
    name="Price_Predictor",
    version= None,
    license= "Apache 2.0",
    description= "Price predictor for houosing"
)

@step(enable_cache=False, experiment_tracker=experiment_tracker.name, model=model)
def model_building_step(
    X_train:pd.DataFrame,y_train:pd.Series
)-> Annotated[Pipeline, ArtifactConfig(name="sklearn_Pipeline", is_model_artifact =True)]:
    """Building and training a linear regression model
    """
    
    #Pretesting
    
    if not isinstance(X_train,pd.DataFrame):
        raise TypeError("X_train must be a pandas Dataframe")
    if not isinstance(y_train,pd.Series):
        raise TypeError("y_train must be a pandas series")
    
    # Identify categorical and Numerical columns
    categorical_cols = X_train.select_dtypes(include=["object","category"])
    numerical_cols = X_train.select_dtypes(exclude=["object","category"])
    
    logging.info("Categorical coulumns:{categorical_cols.tolist()}")
    logging.info("Numerical coulumns:{numerical_cols.tolist()}")
    
    # Defining preprocessing for categorical and numerical features
    numerical_transformer = SimpleImputer(strategy="mean")
    categorical_transformer = Pipeline(
        steps=[
            ("imputer",SimpleImputer(strategy="most_frequent")),
            ("onehot",OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    
    # Bundle preprocessing for numerical and categorical data
    preprocessor = ColumnTransformer(
        transformers=[
            ("num",numerical_transformer,numerical_cols),
            ("cat",categorical_cols,categorical_cols),
        ]
    )
    
    #define model training pipeline
    pipeline =Pipeline(steps=[("preprocessor",preprocessor),("model",LinearRegression())])
    #start an MLFLOW run to log the model training process
    if not mlflow.active_run():
        mlflow.start_run
    try:
        mlflow.sklearn.autolog()
        
        logging.info("Building and training the linear Regression model")
        pipeline.fit(X_train,y_train)
        logging.info("Model training completed.")
        
        #log the coloumns that the model expects
        onehot_encoder = (
            pipeline.named_steps["preprocessor"].transformers_[1][1].named_steps["onehot"]
        )
        onehot_encoder.fit(X_train[categorical_cols])
        expected_cols = numerical_cols.tolist() + list(
            onehot_encoder.get_feature_name_out(categorical_cols)
        )
        logging.info(f"model expects the following columns:{expected_cols}")
        
    except Exception as e:
        logging.error(f"Error During model training{e}")
        raise e
    
    finally:
        mlflow.end_run
        
    return pipeline