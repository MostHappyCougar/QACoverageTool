import os
from abc import ABC, abstractmethod


class AInputProcessor(ABC):
    '''
    Abstraction for input files reading
    '''
    
    def __init__(self, file: os.PathLike):
        self.file = file
    
    @abstractmethod
    def _create_dataframe(self):
        '''
        Just read input file and create dataframe
        '''
        pass




        