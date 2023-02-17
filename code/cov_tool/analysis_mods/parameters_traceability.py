import pandas as pd

from abstractions.analysis import AAnalysis
from input_sockets.input_socket_std import InputSocket
from abstractions.table_formater import IFormatTable

class ParametersTraceability(AAnalysis):
    def __init__(self, mod_params):
        super().__init__(mod_params, InputSocket)
        
        self._index_params = self._mod_params["index"]
        self._columns_params = self._mod_params["columns"]
        self._output_dataframe = pd.DataFrame
    
    
    def analyse(self) -> None:
        self._output_dataframe = pd.crosstab([self._dataframe[ind] for ind in self._index_params], [self._dataframe[col] for col in self._columns_params], 
                                             margins=True, margins_name="_ValuesOccurCount")
        
        
    def format_table(self, formater: IFormatTable) -> None:
        self._output_dataframe = formater.highlite_zero(table=self._output_dataframe)
        self._output_dataframe = formater.make_borders(table=self._output_dataframe)
        self._output_dataframe = formater.format_columns(table=self._output_dataframe)
        self._output_dataframe = formater.format_index(table=self._output_dataframe)
        
        self._output_dataframe = formater.highlite_margins_bot(table=self._output_dataframe)
        self._output_dataframe = formater.highlite_margins_right(table=self._output_dataframe)
        
        
    def pack_results(self) -> tuple:
        self._output_package["path"] = self._mod_params["output_directory"]
        self._output_package["files_name"] = self._mod_params['file_names']
        self._output_package["result"] = self._output_dataframe
        return self._output_package
        