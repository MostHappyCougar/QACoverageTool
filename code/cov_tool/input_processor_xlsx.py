import os

import pandas as pd

from input_processor import AInputProcessor
from input_adapter_std import InputAdapter


class DataFrameMakerXLSX(AInputProcessor):
    '''
    Concrete class to make dataset from XLSX file
    '''

    def __init__(self, file: os.PathLike, sheet: str=None):
        super().__init__(file)
        self._create_dataframe(sheet)
    
    
    def _create_dataframe(self, sheet: str=None) -> None:
        InputAdapter(pd.read_excel(self.file, sheet))