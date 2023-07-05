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

class DataIngestionConfig:
    pass