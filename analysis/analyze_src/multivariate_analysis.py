from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Abstract class for Multivariate Analysis
#----------------------------------------
class MultivariateAnalysisTemp(ABC):
    def analyze(self,df:pd.DataFrame):
        """
        Performs very Comrehensive Multivsriate analysis by generating 

        Args:
            df (pd.DataFrame): _description_
            
        Return:
            None
        """
        self.generate_corelation_heatmap(df)
        self.generate_pairplot(df)
        
    @abstractmethod
    def generate_corelation_heatmap(self,df:pd.DataFrame):
        pass
    
    def generate_pairplot (self,df:pd.DataFrame):
        pass
    
#Concrete class for Multivariate analysis
#----------------------------------------
class SimpleMltivariateAnalysis(MultivariateAnalysisTemp):
    def generate_corelation_heatmap(self, df:pd.DataFrame):
        """
        Generate a corellation heatmap

        Args:
            df (pd.DataFrame): _description_
            
        Return:
            None
        """
        plt.figure(figsize=(12,10))
        sns.heatmap(df.corr(),annot=True,fmt=".2f",cmap="cool",linewidths=0.5)
        plt.title("Corelation Heatmap")
        plt.show()
        
    def generate_pairplot(self, df:pd.DataFrame):
        """
        Generate and display a pair plot for the selecled features

        Args:
            df (pd.DataFrame): _description_
             
        Return:
            None
        """
        sns.pairplot(df)
        plt.suptitle("Pair Plot for Selected Features", y=1.02)
        plt.show()
        
if __name__ == "__main__":
    pass