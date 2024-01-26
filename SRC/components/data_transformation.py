import sys
import os
from SRC.logger import logging
from SRC.exception import CustomException
from SRC.utils import save_object
from dataclasses import dataclass
import numpy as np
import pandas as pd 
from sklearn.pipeline import Pipeline
from sklearn.impute import KNNImputer
from sklearn.preprocessing import RobustScaler
import pickle


@dataclass
class DataTransformationConfig:
        preprocess_file_path=os.path.join('artifacts','preprocess.pkl') # process data file path

# main body
class DataTransformation:
    def __init__(self):
        self.data_Transformation_config=DataTransformationConfig() # link file path and data transformation processs 

    def get_data_transformer(self):
        try:
            logging.info('Data Transformation has started')

            process_pipeline=Pipeline(
                steps=[
                    ('impute',KNNImputer(n_neighbors=5)),
                    ('scaling',RobustScaler())
                ]
            )
            logging.info('pipleline completed')

           
            
            return process_pipeline

        except Exception as e:
            logging.info('Error in Data transformation')
            raise CustomException(e,sys) 

    # starting data transformation
    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            train_df=pd.read_csv(train_data_path)
            test_df=pd.read_csv(test_data_path)

            logging.info('read train and test data completed')
            

            # ## changing columns name
            # train_df=train_df.rename(columns={'Good/Bad':'TARGET_COLUMN'}, inplace=True)
            # test_df=test_df.rename(columns={"Good/Bad": 'TARGET_COLUMN'}, inplace=True)



            # proces pipline
            logging.info(' obitaing process pipline')
            preprocess_obj=self.get_data_transformer()

            target_column_name="Good/Bad"
            
            drop_columns=[target_column_name,'Unnamed: 0']

            

            # Train data x y define
            x_train_df=train_df.drop(columns=drop_columns,axis=1) # X
            y_train_df=train_df[target_column_name] #Y

            # Test data X y define
            x_test_df=test_df.drop(columns=drop_columns,axis=1) # X
            y_test_df=test_df[target_column_name] #Y

            logging.info(
                f'Applying preproceser_obj on traing and test dataframe'
            )

            x_train_arr=preprocess_obj.fit_transform(x_train_df)
            x_test_arr=preprocess_obj.transform(x_test_df)

            train_arr=np.c_[x_train_arr,np.array(y_train_df)]
          
            test_arr=np.c_[x_test_arr,np.array(y_test_df)]
                
            logging.info(f'saved preprocess object. ')
           
            save_object(
                file_path=self.data_Transformation_config.preprocess_file_path,
                obj=preprocess_obj
            )

            logging.info('processor pickel created and saved')
            return(
                train_arr,
                test_arr,
                self.data_Transformation_config.preprocess_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)
