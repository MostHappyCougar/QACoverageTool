import pandas as pd

from abstractions.input_socket import AInputSocket


class InputSocket(AInputSocket):
    '''
    Standard input socket. Will recieve and store datasets made by any input processor
    '''
    
    _dataframe = pd.DataFrame
    
    
    def _set_dataframe(self, dataframe:pd.DataFrame)->None:
        if dataframe.empty():
            raise EmptyDataframeError
        InputSocket._dataframe = dataframe
        
        
    def _get_dataframe(self)->pd.DataFrame:
        self._dataframe_to_return = InputSocket._dataframe
        InputSocket._dataframe = pd.DataFrame
        return self._dataframe_to_return
        
        
class EmptyDataframeError(Exception):
    def __init__(self):
        self.message = f"Dataframe passed to an analysis must be not empty!"
    def __str__(self):
        return self.message