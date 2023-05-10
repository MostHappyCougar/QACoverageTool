import subprocess as sp
import pytest
import os

from common_methods import GLOBAL


class BUser():
    '''
    Base User Class
    '''
    
    _this_file = os.path.dirname(__file__)
    _enter_point_to_utility = os.path.join(_this_file, GLOBAL.GLOBAL.path_from_test_to_util, GLOBAL.GLOBAL.enter_point)
    
    def __init__(self, enter_point: os.PathLike=_enter_point_to_utility):
        self.utility = enter_point
        
    
    def try_to_get_exit_artifacts(self, arguments:list="conf_default", timeout:int=120) -> tuple:
        try:
            self.artifacts = self._get_exit_artifacts(arguments, timeout)
        except sp.TimeoutExpired:
            self._kill_utility_process()
        
        return self.artifacts
        
    
    def _get_exit_artifacts(self, arguments: list, timeout: int) -> tuple:
        self.utility_ran = sp.run(["python", self.utility, *arguments], timeout=timeout, stdout = sp.PIPE, stderr = sp.PIPE)

        self.run_results = {"ReturnCode": self.utility_ran.returncode, 
                            "STDOUT": self.utility_ran.stdout, 
                            "STDERR": self.utility_ran.stderr}   
        return self.run_results
        
        
    def _kill_utility_process(self):
        pytest.fail("Utility runtime is reached the timeout")
        self.utility_ran.kill()
        self.run_results = {}



class User(BUser):
    def __init__(self):
        super().__init__()
        
    
        
