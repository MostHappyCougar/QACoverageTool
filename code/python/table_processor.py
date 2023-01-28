import pandas as pd
import directory_handler
import os

input_file = directory_handler.OutputHandler("tables_to_analisys")
path_to_table = os.path.join(input_file.get_directory(), "test.xlsx")

df = pd.read_excel(path_to_table, "test")



