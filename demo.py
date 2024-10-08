import os

#To check if the mongo db url is set in the Environment variable
# mongo_db_url = os.getenv("MONGODB_URL")
# print(mongo_db_url)

from US_Visa_Approval_System.pipline.training_pipeline import TrainPipeline

obj=TrainPipeline()
obj.run_pipeline()