import pandas as pd

from src.handle_missing_values import (
    DropMissingValStrategy,
    FillMissingValStrategy,
    MissingValueHandler,
)

from zenml import step

@step
def handle_missing_values_step(df:pd.DataFrame,strategy:str="mean") ->pd.DataFrame:
    if strategy =="drop":
        handler =MissingValueHandler(DropMissingValStrategy(axis=0))
        
    elif strategy in ["mean","median","mode","constant"]:
        handler = MissingValueHandler(FillMissingValStrategy(method=strategy))
        
    else:
        raise ValueError(f"Unsupportted Missing Value Handler")
    
    handled_df = handler.execute_handle_missing_values(df)
    return handled_df
