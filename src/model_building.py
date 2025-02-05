import logging
from abc import ABC,abstractmethod
from typing import Any

import pandas as pd
from sklearn.base import RegressorMixin
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# loging
#-------
logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(levelname)s - %(message)s")

#abstract base class for model building
#--------------------------------------
class ModelBuildingStrategy(ABC):
    @abstractmethod
    def build_and_train_model(self,X_train:pd.DataFrame,y_train:pd.Series)-> RegressorMixin:
        """_summary_

        Args:
            X_train (pd.DataFrame): _description_
            y_train (pd.DataFrame): _description_

        Returns:
            RegressorMixin: _description_
        """
        pass
    
#Concrete stratey for lineer Regression using
#--------------------------------------------
class LinearRegressionStrategy(ModelBuildingStrategy):
    def build_and_train_model(self, X_train:pd.DataFrame, y_train:pd.Series):
        """
        Build and train a linear regression model using scikit

        Args:
            X_train (pd.DataFrame): _description_
            y_train (pd.Series): _description_
        """
        if not isinstance(X_train,pd.DataFrame):
            raise TypeError("X_pandas must be a pandas Dataframe")
        if not isinstance(y_train,pd.Series):
            raise TypeError("y_train must be a pandas Series")
        
        logging.info("initializing Linear Regression model with ")
        
        #creating a pipeline
        pipeline = Pipeline(
            [
                ("scaler",StandardScaler()),
                ("model",LinearRegression()),
            ]
        )
        
        logging.info("Trainingh Linear Regression model.")
        pipeline.fit(X_train,y_train)
        
        logging.info("Model Training Completed")
        return pipeline
    
#context Class for model Building
class ModelBuilder:
    def __init__(self,strategy:ModelBuildingStrategy):
        """
        set the strategy for ModelBuilding

        Args:
            strategy (ModelBuildingStrategy): Strategy
        """
        self._strategy =strategy
        
    def set_strategy (self, strategy =ModelBuildingStrategy):
        """
        setting the strategy

        Args:
            strategy (_type_, optional): _description_. Defaults to ModelBuildingStrategy.
        """
        self._strategy =strategy
        
    def build_model(self, X_train:pd.DataFrame,y_train:pd.Series):
        """_summary_

        Args:
            X_train (pd.DataFrame): _description_
            y_train (pd.Series): _description_
        """
        logging.info("Building the Model using the selected strategy")
        return self._strategy.build_and_train_model(X_train,y_train)
    
# Example usage
if __name__ == "__main__":
    # Example dataframe
    # df = pd.read_csv('./extracted_data/AmesHousing.csv')
    # Initialize Model training with a specific strategy
    # X_train = df.drop(columns =['target_col'])
    # y_train = df['target_col']
    # Model_Builder_strategy = ModelBuilder(LinearRegressionStrategy())
    # Model_training = Model_Builder_strategy.build_model(X_train,y_train)
    # print (Model_training.named_steps['model'].coef_)
    pass