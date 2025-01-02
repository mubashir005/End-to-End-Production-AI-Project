from abc import ABC, abstractmethod

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Abstrat Class for  missing values
#---------------------------------
class MissingValuesAnalysisTemplate(ABC):
    def analyze(self, df:pd.DataFrame):
        """_summary_Performs a complete missing values analysis

        Args:
            df (pd.DataFrame): _description_
            
        Return:
            None
        """
        self.identify_missing_values(df)
        self.visualize_missing_values(df)
        
    @abstractmethod
    def identify_missing_values(self, df:pd.DataFrame):
        pass
    
    def visualize_missing_values(self, df:pd.DataFrame):
        pass
    
#Concrete class for missing values analysis
#------------------------------------------
class SimpleMissingValuesAnalysis(MissingValuesAnalysisTemplate):
    def identify_missing_values(self, df:pd.DataFrame):
        print ("\nMissing Values Count by coloumns")
        missing_values = df.isnull().sum()
        print (missing_values[missing_values>0])
        
        
    def visualize_missing_values(self, df:pd.DataFrame):
        print ("\nMissing Values visualization by coloumns")
        plt.figure(figsize=(12,8))
        sns.heatmap(df.isnull(),cbar=False,cmap="viridis")
        plt.title("Missing Valaues Heatmap")
        plt.show()
        
if __name__ == "__main__":
    pass