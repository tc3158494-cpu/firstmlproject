import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join(' aritifact'," train.csv")
    test_data_path: str=os.path.join(' aritifact'," test.csv")
    raw_data_path: str=os.path.join(' aritifact'," data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_Config=DataIngestionConfig()
    def Initiate_data_ingestion(self):
        logging.info(' enterd data  the ingestion methoeds or componenet')
        try:
            f=pd.read_csv('notebooks\data\data')
            logging.info(' read a dataset as dataframe')
            os.makedirs(os.path.dirname(self.ingestion_Config.train_data_path), exist_ok=true)
            df.to_csv(self.ingestion_Config.raw_data_path, index=false,header=true)
            logging.info(' train test split initiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_Config.train_data_path, index=false,header=true)
            test_set.to_csv(self.ingestion_Config.test_data_path, index=false,header=true)
            logging.info(' ingestion of the data is completed')
            return(
                self.ingestion_Config.train_data_path,
                self.ingestion_Config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)
    
if __name__=="__main__":
    obj=DataIngestion()
    obj=initiate_data_ingestion
 