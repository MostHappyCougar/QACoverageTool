from abc import ABC, abstractmethod
import os


class IReadConfig(ABC):
    '''
    Interface that should be relized for configuration parsing. May be relized in different classes that requires to use config
    '''
        
    @abstractmethod    
    def get_parameter(self):
        '''
        Parse configuration and get required parameter
        '''
        pass
    
    
class DefaultConfig():
    '''
    Default config name. Will not contains any methods. Only library of default values
    '''
    default_config = os.path.join("conf_default")