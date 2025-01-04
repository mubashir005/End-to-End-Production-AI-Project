import logging
from abc import ABC,abstractmethod

import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler,OneHotEncoder,StandardScaler

# loging
#-------
logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(levelname)s - %(message)s")

#Abstract Base Class for feature engineering
#-------------------------------------------
class FeatureEngineeringStrategy(ABC):
    @abstractmethod
    def apply_transformation (self, df:pd.DataFrame)->pd.DataFrame:
        """
        Interface to apply feature engineering.Any subclass must apply this method.

        Args:
            df (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """
        pass
    
#Concrete Class to apply log transformation
#------------------------------------------
#applies a logrithmic transformation to normalize the features

class LogTransformation(FeatureEngineeringStrategy):
    def __init__(self,features):
        """
        innitialize with specific features

        Args:
            features (_type_): _description_
        """
        self.features = features
        
    def apply_transformation(self, df:pd.DataFrame) ->pd.DataFrame:
        """
        applies Logtransformation on features for normalization (reduce the skewenes of the data)

        Args:
            df (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """
        logging.info(f"Applying Log Transformation to features")
        df_copy_transformation =df.copy()
        for feature in self.features:
            df_copy_transformation[feature]=np.log1p(
                df[feature]
            ) # apply log on all feature in df_copy_transformation
        logging.info(f" Log Transformation to features Applied")
        return df_copy_transformation
    
#Concrete Class for standard scaling
#-----------------------------------
class StandardScaling(FeatureEngineeringStrategy):
    def __init__(self,features):
        """
        
        initializing the standard scaling with the features (zero meanand unit variance)

        Args:
            features (_type_): _description_
        """
        self.features =features
        self.scaler =StandardScaler()
        
    def apply_transformation(self, df:pd.DataFrame) ->pd.DataFrame:
        """
        standard scaling with the features

        Args:
            df (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """
        logging.info(f"Applying Standard deviantion to the specificx features")
        df_copy_transformation =df.copy()
        df_copy_transformation[self.features]=self.scaler.fit_transform(df[self.features])
        logging.info(f" Standard scalling Applied successfully")
        return df_copy_transformation
    
#Concrete Strategy Class for Min-Max scaling
#-------------------------------------------

class MinMaxScaling(FeatureEngineeringStrategy):
    def __init__(self,features,feature_range=(0,1)):
        """
        initialize the MinMaxScaling withthe specific features

        Args:
            features (_type_): _description_
            feature_range (tuple, optional): _description_. Defaults to (0,1).
        """
        self.features =features
        self.scaler = MinMaxScaler(feature_range=feature_range)
        
    def apply_transformation(self, df:pd.DataFrame) ->pd.DataFrame:
        """
        MinMax scaling

        Args:
            df (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """
        logging.info(f"Applying MinMax scaling to the specificx features")
        df_copy_transformation =df.copy()
        df_copy_transformation[self.features]=self.scaler.fit_transform(df[self.features])
        logging.info(f"MinMax scalling Applied successfully")
        return df_copy_transformation
    
#Concrete Strategy Class for One-Hot encoding for categorical features
#---------------------------------------------------------------------

class OneHotEncoding(FeatureEngineeringStrategy):
    def __init__(self,features):
        """
        for categorical features

        Args:
            features (_type_): _description_
        """
        self.features =features
        self.encoder = OneHotEncoder(sparse=False,drop="first")
        
    def apply_transformation(self, df:pd.DataFrame) ->pd.DataFrame:
        """
        

        Args:
            df (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """
        logging.info(f"Applying OneHot Encoding to the Categorical features")
        df_transformed = df.copy()
        encode_df =pd.DataFrame(
            self.encoder.fit_transform(df[self.features]),
            columns=self.encoder.get_feature_names_out(self.features),
        )
        df_transformed =df_transformed.drop(columns=self.features).reset_index(drop=True)
        df_transformed =pd.concat([df_transformed,encode_df],axis=1)
        logging.info(f"OneHotEncoding Applied successfully")
        return df_transformed
    
# Context Class for Feature Engineering
# -------------------------------------
class FeatureEngineer:
    def __init__(self,strategy =FeatureEngineeringStrategy):
        """
        

        Args:
            strategy (_type_, optional): _description_. Defaults to FeatureEngineeringStrategy.
        """
        self._strategy=strategy
        
    def set_strategy (self,strategy =FeatureEngineeringStrategy):
        self._strategy=strategy
        
    def execute_feature_engineering(self, df:pd.DataFrame) ->pd.DataFrame:
        """
        apply feature enginneering

        Args:
            df (pd.DataFrame): _description_

        Returns:
            pd.DataFrame: _description_
        """
        logging.info("Applying feature engineering strategy.")
        return self._strategy.apply_transformation(df)
    
# Example usage
if __name__ == "__main__":
    # Example dataframe
    # df = pd.read_csv('./extracted_data/AmesHousing.csv')

    # Log Transformation Example
    # log_transformer = FeatureEngineer(LogTransformation(features=['SalePrice', 'Gr Liv Area']))
    # df_log_transformed = log_transformer.execute_feature_engineering(df)
    # print(df_log_transformed)
    # Standard Scaling Example
    # standard_scaler = FeatureEngineer(StandardScaling(features=['SalePrice', 'Gr Liv Area']))
    # df_standard_scaled = standard_scaler.execute_feature_engineering(df)

    # Min-Max Scaling Example
    # minmax_scaler = FeatureEngineer(MinMaxScaling(features=['SalePrice', 'Gr Liv Area'], feature_range=(0, 1)))
    # df_minmax_scaled = minmax_scaler.execute_feature_engineering(df)

    # One-Hot Encoding Example
    # onehot_encoder = FeatureEngineer(OneHotEncoding(features=['Neighborhood']))
    # df_onehot_encoded = onehot_encoder.execute_feature_engineering(df)

    pass