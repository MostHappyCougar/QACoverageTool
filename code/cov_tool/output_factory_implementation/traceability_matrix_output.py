import os

import pandas as pd

from abstractions.save_output import ISaveOutput

class TraceabilityMatrixOutput(ISaveOutput):
    
    def __init__(self, data: tuple):
        self._save_output(data)
        
    
    def _save_output(self, data: tuple):
        
        self._full_path_to_output = os.path.abspath(os.path.join(ISaveOutput.default_path_to_output, data['path']))
        
        if os.path.exists(self._full_path_to_output) == False:
            os.makedirs(self._full_path_to_output)
        
        with pd.ExcelWriter(f"{os.path.join(self._full_path_to_output, data['files_name'])}_param_trace.xlsx") as writer:
            data["data"].to_excel(writer, "ParamsTraceability")
            
        print(f"\nParameters Traceability analysys has been succesfully performed. Actifacts saved upon: {self._full_path_to_output}")