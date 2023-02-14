from abc import ABC, abstractmethod
import os


class ISaveData(ABC):
    '''
    Interface that may be realized to save analysis results
    '''
    
    default_path_to_output = os.path.join(os.path.dirname(__file__), "..", "output")
    
    
    @abstractmethod
    def _save_results(self):
        pass
        
        