import os
import sys
import dill

import pandas as pd
import numpy as np 

from src.exceptions import CustomException

def save_object(file_path, obj):
    # Take the file path and object to create and save a pkl object 
    # inside of that corresponding file path 

    try:
        dir_path = os.path.dirname(file_path)
        
        # If the directory is non-existent, create it 
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

