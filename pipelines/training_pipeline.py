from zenml import Model,pipeline,step
from steps.data_ingestion_step import data_ingestion_step
from steps.handle_missing_values_step import handle_missing_values_step
from steps.feature_engineering_step import feature_engineering_step
from steps.outlier_detection_step import outlier_detection_step
@pipeline(
    model = Model(
        # The name uniquly identifies this model
        name="prices_predictor"
    )
)
def ml_pipeline():
    """end to end machine learning pipeline
    """
    
    #1. Data Ingestion step
    raw_data =data_ingestion_step(
        file_path ="D:/archive.zip"
    )
    
    #2. Handling missing values
    filled_data = handle_missing_values_step(raw_data)
    
    #3. Feature Engineering Step
    engineered_data =feature_engineering_step(
        filled_data, strategy ="log", features =["Gr Liv Area","SalePrice"])
    
    #4. Outliers Detection Step
    Clean_Data = outlier_detection_step(engineered_data,column_name="SalePrice")
    
if __name__ == "__main__":
    # Running the pipeline
    run = ml_pipeline()