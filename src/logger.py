import logging
import os
from datetime import datetime

# Creating a logs directory if it doesn't exist
LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Configuring the logging settings
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# The logger can now be imported and used across the project
