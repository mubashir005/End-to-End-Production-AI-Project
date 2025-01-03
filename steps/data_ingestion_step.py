import pandas as pd
from src.ingest_data import DataIngestorFactory
from zenml import step


@step
def data_ingestion_step(file_path:str) -> pd.DataFrame:
    """
    ingest data from a zip file 

    Args:
        file_path (str): _description_

    Returns:
        pd.DataFrame: _description_
    """
    file_extension ="zip"
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)
    
    df = data_ingestor.ingest(file_path)
    return df