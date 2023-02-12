from abc import ABC, abstractmethod


class IReadConfig(ABC):
    '''
    Interface that should be realized for configuration parsing. May be realized in different classes that require to use config
    '''
    
    default_config = "conf_default"
        
        
    @abstractmethod    
    def get_conf_params(self, conf: str) -> dict:
        '''
        Parse configuration and get required parameter
        '''
        pass