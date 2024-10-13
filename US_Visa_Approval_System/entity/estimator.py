import sys

from pandas import DataFrame
from sklearn.pipeline import Pipeline

from US_Visa_Approval_System.exception import USvisaException
from US_Visa_Approval_System.logger import logging

# Map the target value

class TargetValueMapping:
    def __init__(self):
        self.Certified:int = 0  # Yes
        self.Denied:int = 1     # No
    def _asdict(self): 
        return self.__dict__
    def reverse_mapping(self):
        mapping_response = self._asdict()
        return dict(zip(mapping_response.values(),mapping_response.keys()))
    



