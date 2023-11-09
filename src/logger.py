import logging
import os
from datetime import datetime

#creating `logs folder` in current working directory ---> `.log files` within `logs folder`
os.makedirs(os.path.join(os.getcwd(),"logs"),exist_ok=True)

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"    
LOG_FILE_PATH=os.path.join(os.getcwd(),"logs",LOG_FILE)


#writing logs within `.log files`
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)