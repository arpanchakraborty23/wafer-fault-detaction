import os
import sys
import numpy as np
import pandas as pd 


import pickle
from SRC.exception import CustomException
from sklearn.metrics import accuracy_score
from SRC.logger import logging


def save_object(file_path: str, obj: object) -> None:
        logging.info("Entered the save_object method")

        try:
            with open(file_path, "wb") as file_obj:
                pickle.dump(obj, file_obj)

            logging.info("Exited the save_object method")

        except Exception as e:
            raise CustomException(e, sys)              


def load_obj(file_object):
        try:
            with open(file_path,'rb') as file_obj :
                return pickle.load(file_obj)

        except Exception as e :
            logging.info('Exception occured in load pkl in utils')           
            raise CustomException(e,sys)