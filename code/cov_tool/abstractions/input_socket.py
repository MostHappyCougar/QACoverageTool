from abc import ABC, abstractmethod

import pandas as pd


class AInputSocket(ABC):
    '''
    Abstraction for class that will resieve datasets made by any input processor
    '''
    
    _dataframe = pd.DataFrame
    
    @abstractmethod
    def _set_dataframe(self, dataframe: pd.DataFrame) -> None:
        pass
    
   
    @abstractmethod
    def _get_dataframe(self) -> pd.DataFrame:
        pass
    
    DATAFRAME_TO_ANALYZE = property(_get_dataframe, _set_dataframe)