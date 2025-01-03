from zenml import Model,pipeline,step
from steps.data_ingestion_step import data_ingestion_step
@pipeline(
    model = Model(
        # The name uniquly identifies this model
        name="prices_predictor"
    )
)
def ml_pipeline();
    """end to end machine learning pipeline
    """
    
    #Data Ingestion step
    raw_data =data_ingestion_step(
        file_path ="../data/archive.zip"
    )