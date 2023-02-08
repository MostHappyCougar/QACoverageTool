from abc import ABC, abstractmethod


class Analysis(ABC):
    '''
    Abstract class that describes analysis business requirements
    '''
    
    def __init__(self, config: dict):
        pass
    
    @abstractmethod
    def analyse(self):
        '''
        Analysis main method
        '''
        self.dataframe = None
        pass
        