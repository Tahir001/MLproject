import os
import sys

import pandas as pd
import numpy as np 

from src.exceptions import CustomException

def save_object(file_path, obj):

    try:
        dir_path = os.path.dirname(file_path)
        
