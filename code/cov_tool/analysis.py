from abc import ABC, abstractmethod


class Analysis(ABC):
    
    @abstractmethod
    def analyse(self, dataframe: "DataFrame"):
        pass
        