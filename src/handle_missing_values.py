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
        
        thresh -> Minimum number of non-NaN values required to retain a row or column.

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
        
    def handle(self, df: pd.DataFrame):
        """
        Fill missing values in the rows and columns.

        Args:
            df (pd.DataFrame): Input DataFrame with missing values.

        Returns:
            pd.DataFrame: DataFrame with missing values handled.
        """
        df_cleaned = df.copy()
        
        if self.method == "mean":
            numeric_columns = df_cleaned.select_dtypes(include="number").columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].apply(
                lambda col: col.fillna(col.mean()), axis=0
            )
        elif self.method == "median":
            numeric_columns = df_cleaned.select_dtypes(include="number").columns
            df_cleaned[numeric_columns] = df_cleaned[numeric_columns].apply(
                lambda col: col.fillna(col.median()), axis=0
            )
        elif self.method == "mode":
            for column in df_cleaned.columns:
                if df_cleaned[column].isnull().any():
                    mode_value = df[column].mode()
                    if not mode_value.empty:
                        df_cleaned[column].fillna(mode_value.iloc[0], inplace=True)
        elif self.method == "constant":
            df_cleaned.fillna(self.fill_value, inplace=True)
        else:
            logging.warning(f"Unknown method '{self.method}'. No missing values handled.")

        logging.info("Missing values filled.")
        return df_cleaned
    

    
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