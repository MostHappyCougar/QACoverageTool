import pandas as pd

from abstractions.input_adapter import AInputAdapter


class InputAdapter(AInputAdapter):
    '''
    Standard input adapter. Will recieve and store datasets made by any input processor
    '''
    
    DATAFRAME = pd.DataFrame
    
    def __init__(self, dataframe: pd.DataFrame):
        super().__init__(InputAdapter, dataframe)
