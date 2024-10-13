# The Output that I am getting from fist component is the input for second component


from dataclasses import dataclass

# After Data ingestion Train and Test csv will be generated

@dataclass
class DataIngestionArtifact:
    trained_file_path: str
    test_file_Path: str


@dataclass
class DataValidationArtifact:
    validation_status:bool
    message: str
    drift_report_file_path: str


@dataclass
class DataTransformationArtifact:
    transformed_object_file_path:str 
    transformed_train_file_path:str
    transformed_test_file_path:str


