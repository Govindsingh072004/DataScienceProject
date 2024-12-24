import logging
import os
from datetime import datetime

#log extension and format diya he

LOG_FILE=f"{datetime.now().strftime(' %m_%d_%Y_%H_%M_%S ')}.log"   
#logs file ka name 
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
#agar exist he file to skip
os.makedirs(log_path,exist_ok=True) 

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

#  default logger setup karne ke liye use hota hai
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)