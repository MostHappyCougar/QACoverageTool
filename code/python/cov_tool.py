'''
Enter point to the utility
'''

import table_processor
import analisys
import output_handler
import os

output = output_handler.OutputHandler("output")

states_list = ["state"]
trans_list = ["trans"]
obj_list = ["ord"]
seq_list = ["seq"]

files = "test"
subdir = "test"
output_artifacts = os.path.join(output.get_output_directory(), subdir, files)

state_diagram = analisys.StateTransitionDiagram(table_processor.df, seq_list, obj_list, trans_list, states_list, output_artifacts)
state_diagram.draw_state_transitions_diagram()
state_diagram.fetch_transactions_statistics()