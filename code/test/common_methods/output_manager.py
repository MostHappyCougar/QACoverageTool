import os
import yaml
import time

class ExpectedSTDMessages:
    '''
    Read yaml file with expected stdout and stderr messages
    '''
    def __init__(self, expected_values_list:str="std.yml"):
        self.__curent_file = os.path.dirname(__file__)
        self.__path_to_expected = os.path.join(self.__curent_file, "..", "expected")
        self.__expected = os.path.join(self.__path_to_expected, expected_values_list)
        return
    
    
    def read(self) -> tuple:
        '''
        Open file and read it. Returns a tuple of expected values
        '''
        with open(self.__expected) as stream:
            return yaml.load(stream, yaml.FullLoader)
        
        
        
class FilesManagement:
    '''
    Binary reader of expected and actual files to comparison
    '''
    def __init__(self, files_directory:str):
        self.__curent_file = os.path.dirname(__file__)
        self.__path_to_file = os.path.join(self.__curent_file, files_directory)
        return
    
    
    def read_file(self, file:str) -> str:
        '''
        Read file binary
        '''
        with open(os.path.join(self.__path_to_file, file), "rb") as f:
            return f.read()
        
    
    def remove_files(self, files:list) -> None:
        '''
        It is usefull to remove output files before testing as precondition
        '''
        for file in files:
            self._file = os.path.join(self.__path_to_file, file)
            if os.path.isfile(self._file):
                os.remove(self._file)
        time.sleep(1)
        return
        
            
    