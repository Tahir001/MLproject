import logging
import os 
from datetime import datetime

# Generate a log file for logs w/ corresponding current date 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# We need to give a path on where the files are stored 
logs_path = os.path.join(os.getcwd, "logs", LOG_FILE)
# Make this a directory and append to it if it already exsists 
os.makedirs(logs_path, exist_ok=True)

# Log file full path 
LOG_FILE_PATH  = os.path.join(logs_path, LOG_FILE)

# Setup Logging basic configurations 
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, 
)