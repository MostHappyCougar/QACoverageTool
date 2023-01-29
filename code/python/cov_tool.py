'''
Enter point to the utility
'''
import table_processor
import analisys
import directory_handler
import os
import configs_reader
import sys

out_folder = directory_handler.OutputHandler("output")
output = out_folder.get_directory()
out_folder.directory_createion()

if sys.argv[1] == "std":
    
    #Read config for state-transitions analysis
    _config = configs_reader.Configuration("state_transitions_config.yaml").get_conf_parameters()
    #Get directory foir artifacts saving
    output_artifacts = os.path.join(output, _config["output_files"])
    
    #Table for analysis
    _table = table_processor.SheetToAnalysis(_config["input_directory"], _config["input_table"], _config["input_sheet"])
    #Table converted to dataframe to analysis
    _data = _table.read_table()
    
    
    state_diagram = analisys.StateTransitionDiagram(_data, _config["sequences"], _config["objects"], _config["transitions"], _config["states"], output_artifacts)
    state_diagram.draw_state_transitions_diagram()
    state_diagram.fetch_transactions_statistics()
    
    print(f"\nStates-transitions analysys has been succesfully performed. Actifacts saved upon: {output_artifacts}")
    

