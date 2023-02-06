import os
from abc import ABC, abstractmethod

import pandas as pd


class IInputProcessor(ABC):
    '''
    Interface that shoul be realized to create dataframe from input files
    '''
    
    @abstractmethod
    def create_dataframe(self):
        '''
        Just read input file and create dataframe
        '''
        pass


class DataFrameMaker(IInputProcessor):
    '''
    IInputProcessor realisation for xlsx documents
    '''

    def __init__(self, file: os.PathLike):
        self.file = file
    
    
    def create_dataframe(self, sheet: str=None) -> pd.DataFrame:
        return pd.read_excel(self.file, sheet)

        