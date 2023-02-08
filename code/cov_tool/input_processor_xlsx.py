import os

import pandas as pd

from input_processor import AInputProcessor
from input_adapter_std import InputAdapter


class DataFrameMakerXLSX(AInputProcessor):
    '''
    Class of Input processor for XLSX documents.
    At the class instance created following methods is calling:
    
    _create_dataframe
    _pass_to_adapter
    '''

    def __init__(self, file: os.PathLike, sheet: str=None):
        super().__init__(file)
        self._create_dataframe(sheet)
    
    
    def _create_dataframe(self, sheet: str=None) -> None:
        self.dataframe = pd.read_excel(self.file, sheet)
        super()._pass_to_adapter(InputAdapter)