import sys
import yaml
import os
import numpy as np

from analysis_mods.state_transitions_diagram import StateTransitionsDiagram
from analysis_mods.parameters_traceability import ParametersTraceability
from abstractions.config_reader import IReadConfig
from input_readers.input_reader_xlsx import DataFrameMakerXLSX
from output_factory_implementation.output_factory_imp import OutputFactory
from formaters.table_formater_std import StandardTableFormater


class Main(IReadConfig):
    '''
    Enter point to the utility
    '''
    
    
    @staticmethod
    def get_conf_params(conf) -> dict:
        '''
        Realization of IReadConfig interface to get list of applicable analysis mods
        Analysis mods will be applyied to tests based on this parameters list
        '''
        with open(os.path.join(IReadConfig.default_path_to_configs, conf+".yaml")) as stream:
            return yaml.load(stream, Loader=yaml.SafeLoader)
    
    
    if __name__ == "__main__":
        #Get list of unique configs list
        configs = np.unique(sys.argv[1:])
        
        #When no configs specified then use Default Config
        if len(configs) == 0:
            configs = [IReadConfig.default_config]
        
        #Foreach config
        for conf in configs:
            #Reat config
            CONF_PARAMS = get_conf_params(conf)
            #Perform analysis according to mods specified
            for mod in np.unique(CONF_PARAMS["analysis-mods"]):
                if mod == "state-transition":
                    path_to_input = os.path.join(os.path.dirname(__file__), CONF_PARAMS[mod]["input_directory"], CONF_PARAMS[mod]["input_table"])
                    
                    dataframe_to_analysis = DataFrameMakerXLSX(path_to_input, CONF_PARAMS[mod]["input_sheet"])
                    dataframe_to_analysis.pass_to_socket()
                    
                    STDiag = StateTransitionsDiagram(CONF_PARAMS[mod])
                    STDiag.analyse()
                    analysis_results = STDiag.pack_results()
                    OutputFactory.make_state_trans_output(analysis_results)
                
                if mod == "parameters-traceability":
                    path_to_input = os.path.join(os.path.dirname(__file__), CONF_PARAMS[mod]["input_directory"], CONF_PARAMS[mod]["input_table"])
                    
                    dataframe_to_analysis = DataFrameMakerXLSX(path_to_input, CONF_PARAMS[mod]["input_sheet"])
                    dataframe_to_analysis.pass_to_socket()
                    
                    PTrace = ParametersTraceability(CONF_PARAMS[mod])
                    PTrace.analyse()
                    PTrace.format_table(StandardTableFormater)
                    trace_results = PTrace.pack_results()
                    
                    OutputFactory.make_traceability_output(trace_results)
                    
                    

