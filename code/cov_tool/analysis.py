from abc import ABC, abstractmethod


class Analysis(ABC):
    '''
    Abstract class that describes analysis business requirements
    '''
    
    @abstractmethod
    def analyse(self, dataframe: "DataFrame"):
        '''
        Analysis main method
        '''
        pass
        