import pandas as pd
import numpy as np

from abstractions.analysis import AAnalysis
from input_sockets.input_socket_std import InputSocket
from abstractions.table_formater import IFormatTable

class ParametersTraceability(AAnalysis):
    def __init__(self, mod_params):
        super().__init__(mod_params, InputSocket)
        
        self._index_params = self._mod_params["index"]
        self._columns_params = self._mod_params["columns"]
        
        self._output_dataframe = pd.DataFrame
        
        self._output_pack = {}
        
    
    def analyse(self) -> None:
        self._output_dataframe = pd.crosstab([self._dataframe[x] for x in self._index_params], [self._dataframe[x] for x in self._columns_params])
        
        
    def format_table(self, formater: IFormatTable) -> None:
        self._output_dataframe = formater.highlite_zero(table=self._output_dataframe)
        
        
    def pack_results(self) -> tuple:
        self._output_pack["result"] = self._output_dataframe
        return 
        