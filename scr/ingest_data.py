import os
import zipfile
from abc import ABC, abstractmethod
import pandas as pd

#defining the abstract colass or factory interface for data ingestor
"""this factory calsss will get the data and identify the formate of the data and 
ingest it """
class DataIngester(ABC):
    @abstractmethod
    def ingest(self,file_path:str)->pd.DataFrame:
        """Abstract method to ingest data from a given file."""
        pass
    
"""Now implement the parts of the factory. zip files and others etx..."""
# Implement a class for zip ingestion
class ZipDataIngestor(DataIngester):
    def ingest(self, file_path:str)->pd.DataFrame:
        """extract a zip file and returns the content of the file as pandas DataFrame."""
        
        #file formate check
        if not file_path.endswith(".zip"):
            raise ValueError("The provided file is not a zip file")
        
        #else extract the zip file in the 
        with zipfile.ZipFile(file_path,"r") as zip_ref:
            zip_ref.extractall("extracted_data")
            
        #now look for the extracted csv files
        extracted_files= os.listdir("extracted_data")
        csv_files =[f for f in extracted_files if f.endswith(".csv")]
        
        if len(csv_files)==0:
            raise ValueError("No csv files founds in the folder")
        if len(csv_files)>1:
            raise ValueError("Multiple CSV files found")
        
        #once csv files are being found read the csv files
        
        csv_file_path =os.path.join("extracted_data", csv_files[0])
        df= pd.read_csv(csv_file_path)
        
        #Return the csv file
        return df

#implement the factory
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension:str)->DataIngester:
        """Returns the appropriate data ingestor on basis of the formate provided"""
        if file_extension == ".zip":
            return ZipDataIngestor()
        else:
            raise ValueError("No ingestor available for file extension:{file_extension}")


#example usage
if __name__ == "__main__":
    
    file_path ="data/archive.zip"
    
    file_extension = os.path.splitext(file_path)[1]
    
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)
    
    df = data_ingestor.ingest(file_path)
    
    print(df.head())