from typing import Tuple
import pandas as pd
from src.data_spliting import DataSplitter, SimpleTrainTestSplitStrategy
from zenml import step

@step

def data_splitter_step(
    df:pd.DataFrame,target_col:str
) -> Tuple[pd.DataFrame,pd.DataFrame,pd.Series,pd.Series]:
    """split data in train and test sets"""
    splitter = DataSplitter(strategy=SimpleTrainTestSplitStrategy())
    X_train, X_test, y_train, y_test = splitter.split(df,target_col)
    return X_train, X_test, y_train, y_test