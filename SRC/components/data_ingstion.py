import os
import sys
from SRC.exception import CustomException
from SRC.logger import logging
from SRC.components.data_transformation import DataTransformation
from SRC.components.data_transformation import DataTransformationConfig

import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

## input data store in data ingestion class and use it working of data_ingestion.py

# create data paths to store data
@dataclass
class DataIngestionConfig: #when data requires we go through the Dataingestionconfig
 
    # when input data come as csv store   output in artifacts in file as .csv
    train_data_path: str=os.path.join('artifacts','train.csv') 
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','raw.csv')

# main body
class Dataingestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() # three path save 
    
    # read dataset
    def intiate_data_ingestion(self):
        logging.info('Data ingestion method has started')
        try:
            df=pd.read_csv('notebooks/wafer_23012020_041211.csv') # you also can read data from mongodb frome here
            logging.info('Data transfrom as Datafreame completed')
            
          

            

            # data send to  DataIngestionConfig to store data as train,test,split  
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)  
            
            # save raw data
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info('Train Test Split initiated')
            train_data,test_data=train_test_split(df,test_size=0.25,random_state=40)

            # save train data    
            train_data.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            # save test_data
            test_data.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Data ingestion has compleated')

            return(
                
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
            logging.info('error ocurred')

if __name__=="__main__":
    obj=Dataingestion()
    train_data,test_data=obj.intiate_data_ingestion()            
    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)
    # data_transformation.initiate_data_transformation(test_data)