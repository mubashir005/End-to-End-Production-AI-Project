from abc import ABC,abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Abstract class for Univariate Analysis
#--------------------------------------

class UnivariateAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, df:pd.DataFrame, feature:str):
        """
        Perform Univariate(single coluomn) Analysis on a specific feature

        Args:
            df (pd.DataFrame): _description_
            feature (str): _description_
            
        Returns:
            None
        """
        
#Concrete Analysis numericaal Feature by plotting their distribution
#-------------------------------------------------------------------
class NumericalUnivariateAnalysis(UnivariateAnalysisStrategy):
    def analyze(self, df:pd.DataFrame, feature: str):
        """
        plot the distribution using a histogram or KDE

        Args:
            df (pd.DataFrame): _description_
            feature (str): _description_
        """
        plt.figure(figsize=(10,6))
        sns.histplot(df[feature],kde=True,bins=30)
        plt.title(f"Distribution of{feature}")
        plt.xlabel(feature)
        plt.ylabel("frequency")
        plt.show()
        
#Concrete Categorical Analysis of Features
#-----------------------------------------
class CategoricalUnivariateAnalysis(UnivariateAnalysisStrategy):
    def analyze(self, df:pd.DataFrame, feature:str):
        """
        plots the distribution of a categorical feature using a bar plot

        Args:
            df (pd.DataFrame): _description_
            feature (str): _description_
            
        Returns:
            None
        """
        plt.figure(figsize=(10,6))
        sns.countplot(x=feature, data=df, palette="muted")
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("count")
        plt.xticks(rotation=45)
        plt.show()
        
#context class the UnivariateAnalysisStrategy
#--------------------------------------------
class UnivariateAnalyzer:
    def __init__(self,strategy:UnivariateAnalysisStrategy):
        self._strategy = strategy
        
    def set_strategy(self, strategy: UnivariateAnalysisStrategy):
        self._strategy = strategy
        
    def execute_analysis(self,df:pd.DataFrame,feature:str):
        self._strategy.analyze(df,feature)
        
#Example Uses
if __name__ == "__main__":
    pass
        