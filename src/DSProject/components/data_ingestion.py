import os
import sys
from src.DSProject.exception import CustomException
from src.DSProject.logger import logging
from src.DSProject.utils import read_sql_data
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            # Reading data from SQL database
            logging.info("Fetching data from SQL database...")
            df = read_sql_data()

            logging.info("Creating artifacts directory if not exists...")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw data
            logging.info("Saving raw data...")
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Splitting the data into train and test sets
            logging.info("Splitting data into train and test sets...")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Saving train and test sets
            logging.info("Saving train and test datasets...")
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion is successfully completed.")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            raise CustomException(e, sys)
