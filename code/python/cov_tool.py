'''
Enter point to the utility
'''
import table_processor
import analisys
import directory_handler
import os
import configs_reader
import sys
import numpy as np

#Configs mentioned in run parameters
configs = sys.argv[1:]

#When no configs has been assigned then conf_default.yaml is being used
if bool(sys.argv[1:]) == False:
    configs = "conf_default"
    
#Create output folder
out_folder = directory_handler.OutputHandler("output")
output = out_folder.get_directory()
out_folder.directory_createion()

#Get list of configs
for config in np.unique(configs):
    #Foreach config listed get parameters
    _params = configs_reader.Configuration(f"{config}.yaml").get_conf_parameters()
    for mod in np.unique(_params["analysis-mods"]):
        if mod == "state-transition":
            #Get directory foir artifacts saving
            output_artifacts = os.path.join(output, _params["state-transition"]["output_directory"])
            output_filenames = _params["state-transition"]["file_names"]
            #Get input directory
            _input_directory = _params["state-transition"]["input_directory"]
            #Get table
            _table = _params["state-transition"]["input_table"]
            #Get sheet
            _sheet = _params["state-transition"]["input_sheet"]
            #Sequencer
            _seq = _params["state-transition"]["sequences"]
            #Grouper
            _obj = _params["state-transition"]["objects"]
            #Transitions
            _transitions = _params["state-transition"]["transitions"]
            #States
            _state = _params["state-transition"]["states"]
            
            #Table for analysis
            _table = table_processor.SheetToAnalysis(_input_directory, _table, _sheet)
            #Table converted to dataframe to analysis
            _data = _table.read_table()
            
            #Make analysis artifacts
            state_diagram = analisys.StateTransitionDiagram(_data,_seq, _obj, _transitions, _state, output_artifacts, output_filenames)
            state_diagram.draw_state_transitions_diagram()
            state_diagram.fetch_transactions_statistics()
            print(f"\nStates-transitions analysys has been succesfully performed. Actifacts saved upon: {output_artifacts}")
