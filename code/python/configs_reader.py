import directory_handler
import os
import yaml

class Configuration:
    def __init__(self, config:str):
        self.__config = os.path.join(directory_handler.OutputHandler("configurations").get_directory(), config)
        return
    
    
    def get_conf_parameters(self) -> dict:
        with open(self.__config) as stream:
            return yaml.load(stream, yaml.FullLoader)
        
        



