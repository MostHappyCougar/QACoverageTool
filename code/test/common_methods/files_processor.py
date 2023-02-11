from abc import ABC, abstractmethod
import os
import yaml
import pytest
import pandas as pd


class AFileManager(ABC):
    def __init__(self, files_directory: os.PathLike):
        self.curent_file = os.path.dirname(__file__)
        self.path_to_files = os.path.join(self.curent_file, files_directory)

class IReadFile(ABC):
    @abstractmethod
    def read_file(self, file: str):
        pass

class IFilesDelete(ABC):
    @abstractmethod
    def delete_files(self, files: list[str], fail_if_absence: bool=False) -> None:
        pass
    
    
    
class XLSXReader(AFileManager, IReadFile):
    def __init__(self, files_directory):
        super().__init__(files_directory)
        
      
    def read_file(self, file:str) -> pd.DataFrame:
        return pd.read_excel(os.path.join(self.path_to_files, file))
    
    
    
class YAMLReader(AFileManager, IReadFile):
    def __init__(self, files_directory):
        super().__init__(files_directory)
        
        
        
    def read_file(self, file: str) -> tuple:
        with open(os.path.join(self.path_to_files, file)) as stream:
            return yaml.load(stream, Loader=yaml.SafeLoader)
        
        
        
class BinaryReader(AFileManager, IReadFile):
    def __init__(self, files_directory):
        super().__init__(files_directory)
    

    def read_file(self, file:str):
        with open(os.path.join(self.path_to_files, file), "rb") as f:
                return f.read()
    
    
    
class OutputManager(AFileManager, IFilesDelete):
    def __init__(self, files_directory):
        super().__init__(files_directory)
        

    def delete_files(self, files: list[str], fail_if_absence: bool=False) -> None:
        '''
        It is usefull to remove output files before testing as precondition
        '''
        for file in files:
            self.file = os.path.join(self.path_to_files, file)
            if os.path.isfile(self.file):
                os.remove(self.file)
            elif os.path.isfile(self.file)==False and fail_if_absence==True:
                pytest.fail(f"At the file removal detected {os.path.abspath(self.file)} absense!")
    
        
        
        
    