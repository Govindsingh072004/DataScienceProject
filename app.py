from src.DSProject.logger import logging
import sys
from src.DSProject.exception import CustomException
# from src.DSProject import logger ((both lines are good but muje first wali mast laghi))

from src.DSProject.components.data_ingestion import DataIngestion
from src.DSProject.components.data_ingestion import DataIngestionConfig



if __name__=="__main__":
    logging.info("your Execution started Now Bro..")

    try:
        # data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
    