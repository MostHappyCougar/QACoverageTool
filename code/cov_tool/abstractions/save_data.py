from abc import ABC, abstractmethod


class ISaveData(ABC):
    '''
    Interface that may be realized to save analysis results
    '''
    
    @abstractmethod
    def _save_results(self):
        pass
        
        