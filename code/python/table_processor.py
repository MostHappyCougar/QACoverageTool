import pandas as pd
import directory_handler
import os

class SheetToAnalysis:
    def __init__(self, input_directory:str, table_name:str, sheet_name:str):
        self.__directory = directory_handler.OutputHandler(input_directory)
        self.__path_to_table = os.path.join(self.__directory.get_directory(), table_name)
        self.__sheet = sheet_name
        return
    
    
    def read_table(self) -> "PandasDataFrame":
        return pd.read_excel(self.__path_to_table, self.__sheet)




