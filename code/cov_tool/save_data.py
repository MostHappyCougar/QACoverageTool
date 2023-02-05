from abc import ABC, abstractmethod


class ISaveData(ABC):
    
    @abstractmethod
    def save_results(self):
        pass
        
        