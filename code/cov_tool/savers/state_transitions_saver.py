from abstractions import save_data
import os

from matplotlib import pyplot as plt
import pandas as pd

class StateTransitionsDiagramsSaver(save_data.ISaveData):
    
    def __init__(self, data: tuple):
        self._save_results(data)
    
    
    def _save_results(self, data: tuple):
        
        self._full_path_to_output = os.path.abspath(os.path.join(save_data.ISaveData.default_path_to_output, data['path']))
        
        data["graph"].render(directory=f"{self._full_path_to_output}", view=False)
        
        with pd.ExcelWriter(f"{os.path.join(self._full_path_to_output, data['files_name'])}_path_stats.xlsx") as writer:
            data["stats"].to_excel(writer, "PathStatistics")
            
        fig, (ax1) = plt.subplots()
        ax1.set(title="Path frequency by PathID")
        ax1.pie(x=data["stats"]["Count"], labels=data["stats"].index, autopct='%1.1f%%')
        plt.savefig(f"{os.path.join(self._full_path_to_output, data['files_name'])}_path_stats_vis.pdf")
        
        print(f"\nStates-transitions analysys has been succesfully performed. Actifacts saved upon: {self._full_path_to_output}")