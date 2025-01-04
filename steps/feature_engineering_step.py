from zenml import step
import pandas as pd
from src.feature_engineering import (
    FeatureEngineer,
    LogTransformation,
    MinMaxScaling,
    OneHotEncoding,
    StandardScaling
)

@step
def feature_engineering_step(
df:pd.DataFrame,strategy:str="log",features: list = None
)->pd.DataFrame:
    """
    apply feature_engineering

    Args:
        df (pd.DataFrame): _description_
        strategy (str, optional): _description_. Defaults to "log".
        features (list, optional): _description_. Defaults to None.

    Returns:
        pd.DataFrame: _description_
    """
    if strategy == "log":
        engineer = FeatureEngineer(LogTransformation(features))
    elif strategy == "standard_scaling":
        engineer = FeatureEngineer(StandardScaling(features))
    elif strategy == "minmax_scaling":
        engineer = FeatureEngineer(MinMaxScaling(features))
    elif strategy == "onehot_encoding":
        engineer = FeatureEngineer(OneHotEncoding)
    else:
        raise ValueError(f"Unsupported feature engineering strategy:{strategy} for features: {features}")
    transformed_df = engineer.execute_feature_engineering(df)
    return transformed_df