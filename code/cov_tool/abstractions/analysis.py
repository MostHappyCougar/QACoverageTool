from abc import ABC, abstractmethod

from abstractions.input_adapter import AInputAdapter


class AAnalysis(ABC):
    '''
    Abstract class that describes analysis business requirements
    '''
    
    def __init__(self, config: dict, adapter: AInputAdapter):
        self.mod_params = config
        self.dataframe = adapter.DATAFRAME
    
    @abstractmethod
    def analyse(self) -> None:
        '''
        Analysis main method
        '''
        pass
        