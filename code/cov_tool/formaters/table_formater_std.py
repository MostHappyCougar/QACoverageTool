from abstractions.table_formater import IFormatTable

import pandas as pd

class StandardTableFormater(IFormatTable):
    
    @staticmethod
    def highlite_zero(self, table:pd.DataFrame)->pd.DataFrame:
        pass