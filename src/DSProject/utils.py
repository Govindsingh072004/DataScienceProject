import os
import sys
from sqlalchemy import create_engine
from src.DSProject.exception import CustomException
from src.DSProject.logger import logging
import pandas as pd
from dotenv import load_dotenv
# from sklearn.model_selection import GridSearchCV
# from sklearn.metrics import r2_score
import pickle
import numpy as np

# Load environment variables
load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

# SQLAlchemy connection string
connection_string = f"mysql+pymysql://{user}:{password}@{host}/{db}"

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        # Create SQLAlchemy engine
        engine = create_engine(connection_string)
        
        # Define your query
        query = "SELECT * FROM student"
        
        # Read SQL data into a DataFrame
        df = pd.read_sql_query(query, con=engine)
        
        logging.info("Data reading from MySQL database completed")
        print(df.head())  # For debugging
        
        return df
    except Exception as ex:
        raise CustomException(ex)

# def save_object(file_path, obj):
#     try:
#         dir_path = os.path.dirname(file_path)
#         os.makedirs(dir_path, exist_ok=True)
#         with open(file_path, "wb") as file_obj:
#             pickle.dump(obj, file_obj)
#     except Exception as e:
#         raise CustomException(e, sys)

# def evaluate_models(X_train, y_train, X_test, y_test, models, param):
#     try:
#         report = {}
#         for i in range(len(list(models))):
#             model = list(models.values())[i]
#             para = param[list(models.keys())[i]]

#             gs = GridSearchCV(model, para, cv=3)
#             gs.fit(X_train, y_train)

#             model.set_params(**gs.best_params_)
#             model.fit(X_train, y_train)

#             y_train_pred = model.predict(X_train)
#             y_test_pred = model.predict(X_test)

#             train_model_score = r2_score(y_train, y_train_pred)
#             test_model_score = r2_score(y_test, y_test_pred)

#             report[list(models.keys())[i]] = test_model_score

#         return report
    except Exception as e:
        raise CustomException(e, sys)
