'''
 functionality that i write in a common way wich will be 
 used in the entire app

 value evaluation methods

 example :  read the dataset from a database, create mongo client here
            save my model into the cloud, write my code here
 i will call it, inside the components itself  
 '''

import os
import sys

import numpy as np 
import pandas as pd

from src.exception import CustomException
import dill

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)