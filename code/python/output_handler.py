import os

class OutputHandler:
    def __init__(self, output_path:str):
        self.__this_directory = os.path.dirname(__file__)
        self.__output_directory = output_path
        return
    
    
    def get_output_directory(self) -> str:
        return os.path.join(self.__this_directory, self.__output_directory)
    
        