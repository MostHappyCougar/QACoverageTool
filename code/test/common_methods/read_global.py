import os
import yaml

class GlobalConfig:
    '''
    Read global config
    '''
    def __init__(self, glob:str="GLOBAL.yml"):
        self.__curent_file = os.path.dirname(__file__)
        self.__global_conf = os.path.join(self.__curent_file, glob)
        return 
    
    
    def get_params(self) -> tuple:
        '''
        Get global params. Returns tuple
        '''
        with open(self.__global_conf) as stream:
            return yaml.load(stream, yaml.FullLoader)
        
        