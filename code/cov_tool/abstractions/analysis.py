from abc import ABC, abstractmethod

from abstractions.input_socket import AInputSocket


class AAnalysis(ABC):
    '''
    Abstract class that describes analysis business requirements
    '''
    
    def __init__(self, mod_params: dict, socket: AInputSocket):
        self._mod_params = mod_params
        self._dataframe = socket.DATAFRAME_TO_ANALYZE
        self._output_package = {"path": self._mod_params["output_directory"], "files_name": self._mod_params['files_name'], "data": any}
    
    
    @abstractmethod
    def analyse(self) -> None:
        '''
        Analysis main method
        '''
        pass
    
    
    @abstractmethod
    def pack_results(self) -> dict:
        pass
        