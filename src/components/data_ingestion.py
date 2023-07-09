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
            # Read in our datasets
            df = pd.read_csv('/Users/tahir/Desktop/Github/mlproject/notebook/data/students.csv')
            logging.info('Read the dataset as a dataframe')
            
            # We already know the path to training the data... Lets create folders for this and put our data file there
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header= True)

            # Split the data into train and test sets 
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=10)

            # Save train and test datasets to the configured paths 
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()

