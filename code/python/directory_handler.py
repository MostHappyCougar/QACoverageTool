import os

class OutputHandler:
    def __init__(self, path:str):
        self.__this_directory = os.path.dirname(__file__)
        self.__sub_directory = path
        
        self.__full_path = os.path.join(self.__this_directory, self.__sub_directory)
        return
    
    
    def directory_createion(self) -> None:
        if os.path.exists(self.__full_path) == False:
            print("test")
            os.mkdir(self.__full_path)
        return
    
    
    def get_directory(self) -> str:
        return os.path.join(self.__full_path)
    
        