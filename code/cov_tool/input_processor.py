from abc import ABC, abstractmethod


class IInputProcessor(ABC):
    
    def __init__(self, file: str):
        self.input_file = file
        
        
    @abstractmethod
    def made_dataframe(self):
        pass

        