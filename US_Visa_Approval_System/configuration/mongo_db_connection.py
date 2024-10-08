import sys

from US_Visa_Approval_System.exception import USvisaException
from US_Visa_Approval_System.logger import logging

import os
from US_Visa_Approval_System.constants import DATABASE_NAME, MONGO_CONNECTION_URL
import pymongo
import certifi

ca = certifi.where() # Resolving timeout issue

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                #mongo_db_url="mongodb+srv://babai:babai@visa.sv20u.mongodb.net/?retryWrites=true&w=majority&appName=visa"
                mongo_db_url = os.getenv(MONGO_CONNECTION_URL)  # Get the mongo db url from environment variables,check in demo.py
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGO_CONNECTION_URL} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tls=True, tlsCAFile=ca)  # Mongo Db connection
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection successful")
        except Exception as e:
            raise USvisaException(e,sys)