import logging
from abc import ABC,abstractmethod
import pandas as pd
from sklearn.model_selection import train_test_split


# loging
#-------
logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(levelname)s - %(message)s")

# Abstract class for data spliting
#---------------------------------------

class DataSplittingStrategy(ABC):
    @abstractmethod
    def split_data(self,df:pd.DataFrame,target_col:str):
        """_summary_

        Args:
            df (pd.DataFrame): _description_
            target_col (str): _description_
        """
        pass
    
# Concrete Strategy for simple Train-Test split
#----------------------------------------------
# this strategy do a simple train test splitting

class SimpleTrainTestSplitStrategy(DataSplittingStrategy):
    def __init__(self, test_size =0.2, random_state =42):
        """_summary_

        Args:
            test_size (float, optional): _description_. Defaults to 0.2.
            random_state (int, optional): _description_. Defaults to 42.
            
        
        """
        self.test_size = test_size
        self.random_state =random_state
        
    def split_data(self, df:pd.DataFrame, target_col:str):
        """_summary_

        Args:
            df (pd.DataFrame): _description_
            target_col (str): _description_
        Returns:
            x_train,X_test,Y_train, y_test: traing and testing split
        """
        logging.info("Performing simple train-test split.")
        X = df.drop(columns=[target_col])
        y = df [target_col]
        
        X_train, X_test, y_train, y_test =train_test_split(
            X , y, test_size=self.test_size, random_state=self.random_state
        )
        
        logging.info ("Train-test split completed")
        return X_train, X_test, y_train, y_test
    
#Context class for data spliting
#----------------------------------------------------------
# This class uses a DatasplittingStrategy to split the data
class DataSplitter:
    def __init__(self, strategy:DataSplittingStrategy):
        """
        initializes the datasplitter with a specific data splitting sttrategy

        Args:
            strategy (DataSplittingStrategy): _description_
        """
        self._strategy = strategy
        
    def set_strategy(self, strategy = DataSplittingStrategy):
        """
        set strategy for data splitting

        Args:
            strategy (_type_, optional): _description_. Defaults to DataSplittingStrategy.
        """
        self._strategy = strategy
        
    def split(self,df:pd.DataFrame, target_col:str):
        """
        execute the data splitting

        Args:
            df (pd.DataFrame): _description_
            target_column (str): _description_
            
        Returns:
            x_train,X_test,Y_train, y_test: traing and testing split
        """
        logging.info("Splitting data using the selected strategy")
        return self._strategy.split_data(df,target_col)
    

    
# Example usage
if __name__ == "__main__":
    # Example dataframe
    # df = pd.read_csv('./extracted_data/AmesHousing.csv')
    # Initialize data splitter with a specific strategy
    # data_splitter_strategy = DataSplitter(SimpleTrainTestSplitStrategy(test_size=0.2, random_state=42))
    # X_train, X_test, y_train, y_test = data_splitter_strategy.split(df, target_column='SalePrice')
    pass