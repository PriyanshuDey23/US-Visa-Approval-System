# The Output that I am getting from fist component is the input for second component

from dataclasses import dataclass

# After Data ingestion Train and Test csv will be generated

@dataclass
class DataIngestionArtifact:
    trained_file_path: str
    test_file_file: str
