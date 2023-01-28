'''
Enter point to the utility
'''

import table_processor
import analisys
import directory_handler
import os
import sys

output = directory_handler.OutputHandler("output")

try:
    objects = [sys.argv[1]]
    sequence = [sys.argv[2]]
    transitions = [sys.argv[3]]
    states = [sys.argv[4]]
except IndexError:
    objects, sequence, transitions, states = ["obj"], ["seq"], ["trans"], ["state"]

files = "test"
subdir = "test"

output_artifacts = os.path.join(output.get_directory(), subdir, files)

state_diagram = analisys.StateTransitionDiagram(table_processor.df, sequence, objects, transitions, states, output_artifacts)
state_diagram.draw_state_transitions_diagram()
state_diagram.fetch_transactions_statistics()