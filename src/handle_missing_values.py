import logging
from abc import ABC,abstractmethod
import pandas as pd

# Setup Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s-%(levelname)s - %(message)s")
#Abstratct class for Missing Value handling
#------------------------------------------

class MissingValueHandlingStrategy(ABC):
    @abstractmethod
    def handle(self, df:pd.DataFrame) -> pd.DataFrame:
        """
        abstract method to handle missing values

        Args:
            df (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """
        
        pass
    
#Concrete strategy for dropping Missing Value
#--------------------------------------------
class DropMissingValStrategy(MissingValueHandlingStrategy):
    def __init__(self, axis=0,thresh=None):
        """
        axis weather to drop rows or columns
        axis = 0 MEANS drop Rows
        
        thresh -> Min number of Nan values require to keep the row and coloumns

        Args:
            axis (int, optional): _description_. Defaults to 0.
            thresh (_type_, optional): _description_. Defaults to None.
        """
        self.axis =axis
        self.thresh =thresh
        
    def handle(self, df:pd.DataFrame) ->pd.DataFrame:
        """
        drop missing values from row or coloumns

        Args:
            df (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """
        logging.info ("Dropping Missing values with axis = {self.axis} and Thresh = {self.thresh}")
        df_drop = df.dropna(axis=self.axis,thresh=self.thresh)
        logging.info("Missing Values Dropped")
        return df_drop
    
#Concrete strategy for Filling Missing Value
#--------------------------------------------
class FillMissingValStrategy(MissingValueHandlingStrategy):
    def __init__(self,method ="mean", fill_value=None):
        """
        Fill missing values in rows or coloumns

        Args:
            method (str, optional): _description_. Defaults to "mean".
            fill_value (_type_, optional): _description_. Defaults to None.
        """
        self.method=method
        self.fill_value= fill_value
        
    def handle(self, df:pd.DataFrame):
        """
        Fill missing values in the rows and coluomns

        Args:
            df (pd.DataFrame): _description_
        """
        logging.info ("Filling Missing values with Method = {self.method} and fill_value = {self.fill_value}")
        df_fill = df.copy()
        if self.method =="mean":
            numericcol =df_fill.select_dtypes(include="number").columns
            df_fill[numericcol] =df_fill[numericcol].fillna(
                df[numericcol].mean()
            )
            
            
        elif self.method =="median":
            numericcol =df_fill.select_dtypes(include="number").columns
            df_fill[numericcol] =df_fill[numericcol].fillna(
                df[numericcol].median()
            )
            
        elif self.method =="mode":
            for column in df_fill.columns:
                df_fill[column].fillna(df[column].mode().iloc(0),inplace="True")
        
        elif self.method =="constant":
            df_fill=df_fill.fillna(self.fill_value)
            
        else:
            logging.warning(f"Unknown Mewthod '{self.method}'.None")
            
        logging.info("Missing Values filled")
        return df_fill
    
#Context Class
#-------------

class MissingValueHandler:
    def __init__(self,strategy:MissingValueHandlingStrategy):
        self._strategy = strategy
        
    def set_strategy(self,strategy:MissingValueHandlingStrategy):
        logging.info(f"Setting Missing Value Stratgy")
        self._strategy =strategy
        
    def execute_handle_missing_values(self,df:pd.DataFrame)-> pd.DataFrame:
        return self._strategy.handle(df)
    
if __name__ == "__main__":
    pass