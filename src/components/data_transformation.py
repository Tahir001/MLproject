# Import standard libraries 
import sys
import os
import pandas as pd
import numpy as np

# Data class
from dataclasses import dataclass

# Data Transformations 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# MLops
from src.exceptions import CustomException
from src.logger import logging
from src.utils import save_object

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
        # This function is responsible for data transformation 
        # Create all of my pkl files which are responsible for our data transformation
        try:
            # Must do EDA before this
            numericical_columns = ['writing_score', 'reading_score']
            categorical_columns = [
                'gender', 
                'race_ethnicity',
                'parental_level_of_education',
                'lunch',
                'test_preparation_course'
            ]

            # Create a pipeline for numerical columns
            # Impute the numerical columns using median, and then scale the features 
            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )

            # Create a pipeline for catergorical columns
            # Impute missing values, encode categorical vars, and scale them 
            cat_pipeline = Pipeline(
                steps = [
                    # Replace missing values with mode
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    # One hot encoder as there isn't many categories for each class
                    ('one_hot_encoder', OneHotEncoder()),
                    ('scaler', StandardScaler(with_mean=False))
                ]
            )

            logging.info("Numerical  Columns standard scaling completed")
            logging.info("Categorical Columns encoding completed")

            # Combine our numerical and categorical transformations
            # Use Column transformer for this
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numericical_columns),
                    ("cat_pipeline", cat_pipeline, categorical_columns)
                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data completed")

            # Read in our preprocessing object 
            logging.info ("Obtaining preprocessing object")
            preprocessing_obj = self.get_data_transformer_object()

            # Get independent and dependent variable(s)
            target_column_name = 'math_score'
            numerical_columns= ['writing_score', 'reading_score']

            # Drop the target variable from train and test data 
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            # Do the same for test data 
            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            # Preprocessing_obj is an instance of get_data_transformer_object(), 
            # which is used to transform the input features (train and test sets) using defined transformations 
            # fit_transform() applies the pre-processing defined in the instance onto the input array
            # and then transform that input array based on the fit. 
            # Then, we transform the test data using the same fit we got from the train data  
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            # Get train and test arrays 
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(
                # Save this preprocessed object using our save function from utils.py  
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        
        except Exception as e:
            raise CustomException(e, sys) 