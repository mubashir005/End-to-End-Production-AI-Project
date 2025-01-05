import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import logging
from abc import ABC,abstractmethod

#Loging Setup
#------------
logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(levelname)s - %(message)s")

#Abstartct Class for Outlier Detection strategy
#----------------------------------------------
class OutlierDetectionStrategy(ABC):
    @abstractmethod
    def detect_outliers(self, df:pd.DataFrame) ->pd.DataFrame:
        """
        Abstract method to detect outliers 

        Args:
            df (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """
        pass
    
#Concrete Class for ZScore based Outlier Detection strategy
#----------------------------------------------------------
class ZScoreOutliersDetection(OutlierDetectionStrategy):
    def __init__(self,threshold=3):
        """
        How far a datapoint is away from the mean of the data set

        Args:
            threshold (int, optional): _description_. Defaults to 3.
        """
        self.threshold = threshold
        
    def detect_outliers(self, df:pd.DataFrame)->pd.DataFrame:
        logging.info("Detecting Outliers using the Zscore")
        z_scrore =np.abs((df-df.mean())/df.std())
        Outliers = z_scrore >self.threshold
        logging.info("Outliers Detected using the Zscore")
        return Outliers
    
#Concrete Class for IQR based Outlier Detection strategy
#-------------------------------------------------------
class IQROutliersDetection(OutlierDetectionStrategy):
    def detect_outliers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        If the datapoint is above or below the viscur/beyond the upper 
        and lower fense its an outlier like in BOX Plot

        Args:
            df (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """
        logging.info("Detecting Outliers using the IQR Method")
        Q1 = df.quantile(0.25)
        Q3 = df.quantile (0.75)
        IQR = Q3 -Q1
        Outliers = (df <(Q1 -1.5*IQR)) | (df > (Q3 + 1.5*IQR))
        logging.info("Outliers Detected using the IQR Method")
        return Outliers
    
#Context Class that detects and handle the outliers
#--------------------------------------------------
class OutlierDetector:
    def __init__(self,strategy:OutlierDetectionStrategy):
        self._strategy =strategy
        
    def set_strategy(self,strategy:OutlierDetectionStrategy):
        logging.info("Switching the strategy")
        self._strategy =strategy
    
    def detect_outliers(self, df:pd.DataFrame) ->pd.DataFrame:
        return self._strategy.detect_outliers(df)
    
    def handle_outliers(self, df:pd.DataFrame,method ="remove",**kwargs)->pd.DataFrame:
        outliers = self.detect_outliers(df)
        if method =="cap":
            logging.info("caping outliers from the data set")
            df_cleaned =df.clip(lower=df.quantile(0.01),upper=df.quantile(0.99),axis=1)
        elif method =="remove":
            logging.info("removing outliers from the data set")
            df_cleaned = df[(~outliers).all(axis=1)]
        else:
             logging.info("Unvalid method '{method}'. No outliers")
             
        logging.info("Outlier Handling Completed")
        return df_cleaned
    
    def visulize_outliers (self,df:pd.DataFrame,features:list):
        logging.info("visualizig outliers for the features:{features}")
        for feature in features:
            plt.figure(figsize=(10,6))
            sns.boxplot(x=df[feature])
            plt.title(f"Boxplot of {feature}")
            plt.show()
            
        logging.info("Outliers Visualization completed")
        
# Example usage
if __name__ == "__main__":
    # # Example dataframe
    # df = pd.read_csv("./extracted_data/AmesHousing.csv")
    # df_numeric = df.select_dtypes(include=[np.number]).dropna()

    # # Initialize the OutlierDetector with the Z-Score based Outlier Detection Strategy
    # outlier_detector = OutlierDetector(ZScoreOutliersDetection(threshold=3))

    # # Detect and handle outliers
    # outliers = outlier_detector.detect_outliers(df_numeric)
    # df_cleaned = outlier_detector.handle_outliers(df_numeric, method="remove")

    # print(df_cleaned.shape)
    # # Visualize outliers in specific features
    # outlier_detector.visulize_outliers(df_cleaned, features=["SalePrice", "Gr Liv Area"])
    pass

