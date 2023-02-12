import os

import pandas as pd

from abstractions.input_reader import AInputReader
from input_sockets.input_socket_std import InputSocket


class DataFrameMakerXLSX(AInputReader):
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
        self._dataframe = pd.read_excel(self._file, sheet)
        super()._pass_to_socket(InputSocket)