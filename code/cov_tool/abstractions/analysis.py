from abc import ABC, abstractmethod

from abstractions.input_adapter import AInputAdapter


class AAnalysis(ABC):
    '''
    Abstract class that describes analysis business requirements
    '''
    
    def __init__(self, mod_params: dict, adapter: AInputAdapter):
        self._mod_params = mod_params
        self._dataframe = adapter.DATAFRAME
    
    @abstractmethod
    def analyse(self) -> None:
        '''
        Analysis main method
        '''
        pass
        