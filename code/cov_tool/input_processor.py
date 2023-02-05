from abc import ABC, abstractmethod
import os


class IInputProcessor(ABC):
    
        
    @abstractmethod
    def create_dataframe(self):
        pass

        