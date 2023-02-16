import pandas as pd

from abstractions.analysis import AAnalysis
from abstractions.save_data import ISaveData
from input_adapters.input_adapter_std import InputAdapter

class ParametersTrassobility(AAnalysis, ISaveData):
    def __init__(self, mod_params):
        super().__init__(mod_params, InputAdapter)
        
        self.index_params = self._mod_params["index"]
        self.columns_params = self._mod_params["columns"]
        self.values = self._Amod_params["values"]
        
    
    def analyse(self) -> None:
        pd.pivot_table(self.dataframe, values=self.values, index=self.index_params, columns=self.columns_params)
        