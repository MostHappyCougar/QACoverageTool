import os
import pandas as pd

from input_processor import IInputProcessor

class DataFrameMaker(IInputProcessor):

    def __init__(self, file: os.PathLike):
        self.file = file
    
    
    def create_dataframe(self, sheet: str=None) -> pd.DataFrame:
        return pd.read_excel(self.file, sheet)

        