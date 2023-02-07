import sys
import yaml
import os
import numpy as np

from state_transitions_diagram import StateTransitionsDiagram
from config_reader import IReadConfig
from input_processor_xlsx import DataFrameMakerXLSX


class Main(IReadConfig):
    '''
    Enter point to the utility
    '''
    
    
    @staticmethod
    def get_parameter(conf) -> list:
        '''
        Realization of IReadConfig interface to get list of applicable analysis mods
        Analysis mods will be applyied to tests based on this parameters list
        '''
        with open(os.path.join(os.path.dirname(__file__), "configurations", conf+".yaml")) as stream:
            return yaml.load(stream, yaml.FullLoader)
    
    
    if __name__ == "__main__":
        #Get list of unique configs list
        configs = np.unique(sys.argv[1:])
        
        #When no configs specified then use Default Config
        if len(configs) == 0:
            configs = [IReadConfig.default_config]
        
        #Foreach config
        for conf in configs:
            #Perform analysis according to mods specified
            for mod in np.unique(get_parameter(conf)["analysis-mods"]):
                if mod == "state-transition":
                    
                    path_to_input = os.path.join(os.path.dirname(__file__), 
                                                get_parameter(conf)["state-transition"]["input_directory"], 
                                                get_parameter(conf)["state-transition"]["input_table"])
                    
                    DataFrameMakerXLSX(path_to_input, get_parameter(conf)["state-transition"]["input_sheet"])
                    
                    STDiag = StateTransitionsDiagram(get_parameter(conf))
                    STDiag.analyse()

