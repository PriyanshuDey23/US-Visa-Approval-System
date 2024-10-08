import os
from datetime import date

DATABASE_NAME="US_Visa"
COLLECTION_NAME='Visa_Data'
MONGO_CONNECTION_URL="MONGODB_URL" # Save the url in Environment variable and load it with the help of os
PIPELINE_NAME:str ="usvisa"
ARTIFACT_DIR:str= "Artifact"
MODEL_FILE_NAME='model.pkl'
FILE_NAME: str="Us_Visa.csv" # After downloading the data
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "Visa_Data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2