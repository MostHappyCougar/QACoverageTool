from abc import ABC

import pandas as pd


class AInputAdapter(ABC):
    '''
    Abstraction for class that will resieve datasets made by any input processor
    '''
    
    DATAFRAME = pd.DataFrame
    
    def __init__(self, cls, dataframe: pd.DataFrame):
        cls.DATAFRAME = dataframe