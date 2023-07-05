# Import standard libraries 
import os 
import sys 
import pandas as pd
import numpy as np

# Data Pre-processing 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Import custom exceptions and logging functions 
from src.exceptions import CustomException
from src.logger import logging

@dataclass
class DataIngestionConfig:
    # Inputs that we're giving to our data ingestion component -> Now it knows where to save these files
    train_data_path: str=os.path.join("artifacts", "train.csv")
    test_data_path: str=os.path.join("artifacts", "test.csv")
    raw_data_path: str=os.path.join("artifacts", "data.csv")

class DataIngestion:
    def __init__(self):
        # The three paths will be stored in our variable here 
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        # Start our data ingestion process 
        logging.info("Entered the Data Ingestion Method or Component")
        try:
            df = pd.read_csv('')
        except:
            pass



