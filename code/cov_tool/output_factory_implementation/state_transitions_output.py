from abstractions.save_output import ISaveOutput
import os

from matplotlib import pyplot as plt
import pandas as pd

class StateTransitionsDiagramOutput(ISaveOutput):
    
    def __init__(self, data: tuple):
        self._save_output(data)
    
    
    def _save_output(self, data: tuple):
        
        self._full_path_to_output = os.path.abspath(os.path.join(ISaveOutput.default_path_to_output, data['path']))
        
        if os.path.exists(self._full_path_to_output) == False:
            os.makedirs(self._full_path_to_output)
        
        data["data"]["graph"].render(directory=f"{self._full_path_to_output}", view=False)
        
        with pd.ExcelWriter(f"{os.path.join(self._full_path_to_output, data['files_name'])}_path_stats.xlsx") as writer:
            data["data"]["stats"].to_excel(writer, "PathStatistics")
            
        fig, (ax1) = plt.subplots()
        ax1.set(title="Path frequency by PathID")
        ax1.pie(x=data["data"]["stats"]["Count"], labels=data["data"]["stats"].index, autopct='%1.1f%%')
        plt.savefig(f"{os.path.join(self._full_path_to_output, data['files_name'])}_path_stats_vis.pdf")
        
        print(f"\nStates-transitions analysys has been succesfully performed. Actifacts saved upon: {self._full_path_to_output}")