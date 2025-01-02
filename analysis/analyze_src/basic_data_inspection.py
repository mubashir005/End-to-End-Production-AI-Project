from abc import ABC, abstractmethod
import pandas as pd

#Abstract slass

class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self, df: pd.DataFrame):
        """
        perform inspection on the data
        
        Args:
            df (pd.DataFrame): the dataframe on which inspection is being done
            
        returns:
            None: This method print the inspection results
        """
        pass
    
#Concrete Strategy  for Data tyes inspection
#-------------------------------------------
class DataTypeInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        """
        inspect and prints data types and counts null

        Args:
            df (pd.DataFrame): 
        """
        print("\nData Types and Non-null Counts")
        print(df.info)
        
#Concrete Strategy for Summary statistics
#-------------------------------------------

class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df:pd.DataFrame):
        """Print _summary_ statics for numerical and categorical

        Args:
            df (pd.DataFrame):
        """
        print("\nSummary Statetistics (Numerical Features:)")
        print(df.describe)
        print("\nSummary Statetistics (Categorical Features:)")
        print(df.describe(include=["O"]))
        
# Context Class that uses a DataInspectionStrategy or factory class
#------------------------------------------------------------------
#Switch between the strategies
class DataInspector:
    def __init__(self, strategy:DataInspectionStrategy):
        """
        Initialize the DataInspector with a specific data inspector

        Args:
            strategy (DataInspectionStrategy): 
        return:
            None
        """
        
        self._strategy = strategy
        
    def set_strategy(self, strategy: DataInspectionStrategy):
        """
        Sets a new strategy for the DataInspector.

        Parameters:
        strategy (DataInspectionStrategy): The new strategy to be used for data inspection.

        Returns:
        None
        """
        self._strategy = strategy
        
    def execute_inspection(self,df:pd.DataFrame):
        self._strategy.inspect(df)

#Example Uses
if __name__ == "__main__":
    pass