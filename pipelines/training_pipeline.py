from zenml import Model,pipeline,step
from steps.data_ingestion_step import data_ingestion_step
from steps.handle_missing_values_step import handle_missing_values_step
@pipeline(
    model = Model(
        # The name uniquly identifies this model
        name="prices_predictor"
    )
)
def ml_pipeline():
    """end to end machine learning pipeline
    """
    
    #Data Ingestion step
    raw_data =data_ingestion_step(
        file_path ="D:/archive.zip"
    )
    
    #handling missing values
    filled_data = handle_missing_values_step(raw_data)
    
    
    
    
if __name__ == "__main__":
    # Running the pipeline
    run = ml_pipeline()