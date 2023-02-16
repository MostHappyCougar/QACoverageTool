import os
from abc import ABC, abstractmethod

from abstractions.input_socket import AInputSocket


class AInputReader(ABC):
    '''
    Abstraction for input files reading
    '''
    
    def __init__(self, file: os.PathLike):
        self._file = file
        self._dataframe = None
    
    
    @abstractmethod
    def _create_dataframe(self) -> None:
        '''
        Dataframe creation logic
        '''
        pass
    
    
    def pass_to_socket(self, socket: AInputSocket) -> None:
        '''
        This method must be called to pass dataframe to a socket
        '''
        socket.DATAFRAME_TO_ANALYZE = self._dataframe




        