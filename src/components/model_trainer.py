# Standard libraries
import os
import sys
from dataclasses import dataclass

# Models and Metrics
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor, 
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

# MLOps 
from src.exceptions import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models

@dataclass
class ModelTrainerConfig:
    # Define configurations -> path for where to save the trained model
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    # Define a Model Trainer class which is responsible for training our model
    def __init__(self):
        # Get the configurations from the class above
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            # Log some info
            logging.info("Splitting training and test input data")
            X_train, y_train, X_test, y_test = ( 
                # Extract all of the columns besides last for training
                # Extract the last column and store it in the y variables 
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:, -1]
            )
            # Get models
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                             models=models)

            ## To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            ## To get best model name from dict
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            # If our model is not good as atleast 60%.. We can say no best model found
            if best_model_score<0.6:
                raise CustomException("No best model found")
            logging.info(f"Best found model on both training and testing dataset")

            # Save our best trained model
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            # Get the best models predicted value and evaluate the accuracy
            predicted=best_model.predict(X_test)
            r2_square = r2_score(y_test, predicted)
            return r2_square
        
        except Exception as e: 
            raise CustomException(e, sys)
