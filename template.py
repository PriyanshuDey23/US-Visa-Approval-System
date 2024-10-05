import os
from pathlib import Path  
import logging

# Creating Logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:') # current time- asctime, along with the 

project_name="US_Visa_Approval_System" # As Per Requirement

# List of Files and Folder need to be created

list_of_files=[
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "config/model.yaml",
    "config/schema.yaml",
]




for filepath in list_of_files:
    filepath= Path(filepath) # define the path type, it will ignore the(/) and create the files and folder
    filedir,filename=os.path.split(filepath)# For Separating the file and Folder name

    # Create the directory
    if filedir != "":       # Not  empty,present(if folder is present)
        os.makedirs(filedir,exist_ok=True) # Make directory, exist_ok=True:- If it is created then it won't be created again
        logging.info(f" Creating Directory ; {filedir} for the file: {filename}")

    # Creating the files
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): # Check  file not exists or check the size of the file,if it is empty ,if it is not empty then it will not replace it

        with open(filepath, "w" ) as f: # Create that file
            pass
            logging.info(f"Creating Empty File: {filepath}")


    else:
        logging.info(f"{filename} is already exists ")

# All Files And Folder will be created