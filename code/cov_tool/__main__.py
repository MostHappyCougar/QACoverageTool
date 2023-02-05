import sys
import yaml
import os

from state_transitions_diagram import StateTransitionsDiagram
from config_reader import DefaultConfig, IReadConfig

class Main(IReadConfig):
    
    @staticmethod
    def get_parameter(conf) -> list:
        with open(os.path.join(os.path.dirname(__file__), "configurations", conf+".yaml")) as stream:
            return yaml.load(stream, yaml.FullLoader)["analysis-mods"]
    
    
    if __name__ == "__main__":
        configs = sys.argv[1:]
        
        if len(configs) == 0:
            configs = [DefaultConfig.default_config]
        
        for conf in configs:
            for mod in get_parameter(conf):
                if mod == "state-transition":
                    STDiag = StateTransitionsDiagram(conf)
                    STDiag.analyse()

