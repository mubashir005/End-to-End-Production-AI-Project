from zenml import step
import pandas as pd
import logging
from src.outlier_detection import(
    OutlierDetectionStrategy,
    ZScoreOutliersDetection,
    IQROutliersDetection,
    OutlierDetector
)

@step
def outlier_detection_step(df:pd.DataFrame,column_name:str) -> pd.DataFrame:
    logging.info("Starting Outlier Detection")
    if df is None:
        logging.info("recieved a NoneType dataframe")
        raise ValueError("df Must be a non-null dataframe")
    if not isinstance(df,pd.DataFrame):
        raise ValueError("the input df mudt be pandas dataframe")
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    df_numeric = df.select_dtypes(include=[int, float])
    
    outlier_detector =OutlierDetector(ZScoreOutliersDetection(threshold=3))
    outliers = outlier_detector.detect_outliers(df_numeric)
    df_cleaned = outlier_detector.handle_outliers(df_numeric,method= "remove")
    return df_cleaned