import os
from abc import ABC, abstractmethod

from abstractions.input_adapter import AInputAdapter


class AInputProcessor(ABC):
    '''
    Abstraction for input files reading
    '''
    
    def __init__(self, file: os.PathLike):
        self.file = file
        self.dataframe = None
    
    
    @abstractmethod
    def _create_dataframe(self) -> None:
        '''
        Dataframe creation logic
        '''
        pass
    
    
    def _pass_to_adapter(self, adapter: AInputAdapter) -> None:
        '''
        This method must be called to pass dataframe to an adapter
        '''
        adapter.DATAFRAME = self.dataframe




        