# Import standard libraries 
import sys
import os
import pandas as pd
import numpy as np

from dataclasses import dataclass

# Data Transformations 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# MLops
from src.exceptions import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    """
    Gives us any path or input that we will be requiring for our data & transformation component 
    """
    # To save any models in a pkl file, for this we need a specific pkl path 
    # You can also do the same for model file 
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    # Give the input from above to here
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        # Create all of my pkl files which are responsible for our data transformation
        try:
            # Must do EDA before this
            numerocical_columsn = ['writing_score', 'reading_score']
            categorical_columns = [
                'gender', 
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preperation_course'
            ]

            # Create a pipeline for numerical columns
            # Impute the numerical columns using median, and then scale the features 
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median'))
                    ('scaler', StandardScaler())
                ]
            )
            
            # Create a pipeline for catergorical columns
            # Impute missing values, encode categorical vars, and scale them 
            cat_pipeline = Pipeline(
                steps = [
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder', OneHotEncoder()),
                    ('scaler', StandardScaler())
                ]
            )
            
        except:
            pass

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = 


    def __init__(self): 



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

