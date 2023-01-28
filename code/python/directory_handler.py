import os

class OutputHandler:
    def __init__(self, path:str):
        self.__this_directory = os.path.dirname(__file__)
        self.__sub_directory = path
        return
    
    def get_directory(self) -> str:
        return os.path.join(self.__this_directory, self.__sub_directory)
    
        