from abc import ABC,abstractmethod
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Abstract class for Bivariate Analysis
#--------------------------------------

class BivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze (self, df:pd.DataFrame, feature1:str, feature2:str):
        """
        Bivariate Analysis between two features feature1 and feature2

        Args:
            df (pd.DataFrame): _description_
            feature1 (str): _description_
            feature2 (str): _description_
            
        return:
            None
        """
        pass
    
#Concrete Strategy for  Numerical Analysis vs Numerical Analysis
#---------------------------------------------------------------

class NumericalBiVariateAnalysis(BivariateAnalysisStrategy):
    def analyze(self, df:pd.DataFrame, feature1:str, feature2:str):
        """
        Bivariate Numerical analysis between two features using scatter plot

        Args:
            df (pd.DataFrame): _description_
            feature1 (str): _description_
            feature2 (str): _description_
        """
        plt.figure(figsize=(10,6))
        sns.scatterplot(x=feature1,y=feature2,data=df)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.show()
        
#Concrete Strategy for  Categorical Analysis vs Numerical Analysis
#-----------------------------------------------------------------
class CategoticalBiVariateAnalysis(BivariateAnalysisStrategy):
    def analyze(self, df:pd.DataFrame, feature1:str, feature2:str):
        """
        Plot a relationship between a Categorical feature and Numerical Feature

        Args:
            df (pd.DataFrame): _description_
            feature1 (str): _description_
            feature2 (str): _description_
        """
        plt.figure(figsize=(10,6))
        sns.boxenplot(x=feature1,y=feature2,data=df)
        plt.title(f"{feature1} vs {feature2}")
        plt.xlabel(feature1)
        plt.ylabel(feature2)
        plt.xticks(rotation=45)
        plt.show()
        


#context class the BivariateAnalysisStrategy
#--------------------------------------------

class BivariateAnalyzer:
    def __init__(self, strategy:BivariateAnalysisStrategy):
        self._strategy =strategy
        
    def set_strategy (self, strategy:BivariateAnalysisStrategy):
        self._strategy =strategy
        
    def execute_analysis (self, df:pd.DataFrame,feature1:str,feature2:str):
        self._strategy.analyze(df,feature1,feature2)
        
#Example Uses
if __name__ == "__main__":
    pass