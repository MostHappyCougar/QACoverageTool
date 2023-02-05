from abc import ABC, abstractmethod
import os


class IReadConfig(ABC):
        
    @abstractmethod    
    def get_parameter(self):
        pass
    
    
class DefaultConfig():
    default_config = os.path.join("conf_default")