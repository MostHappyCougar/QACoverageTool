import subprocess as sp
import pytest
import os

from common_methods import GLOBAL

class User(object):
    '''
    Main user actions. It is usefull to emulate user actions related to the utility
    '''
    #Read global parameters
    _this_file = os.path.dirname(__file__)
    _path_to_enter_point = os.path.join(_this_file, GLOBAL.GLOBAL.path_from_test_to_util, GLOBAL.GLOBAL.enter_point)
    
    
    def __init__(self, utility:str=_path_to_enter_point):
        self.__utility = utility
        return 
    
    
    def try_to_run(self, arguments:list="conf_default", timeout:int=5) -> tuple:
        '''
        Just run utility or driver on behalf user. Returns tuple of captured Return Code, STDOIUT and STDERR as bytes
        '''
        try:
            self.__utility_ran = sp.run(["python", self.__utility, *arguments], timeout=timeout, stdout = sp.PIPE, stderr = sp.PIPE)
            #Tuple of captured things
            self.__run_results = {"ReturnCode": self.__utility_ran.returncode, 
                                  "STDOUT": self.__utility_ran.stdout, 
                                  "STDERR": self.__utility_ran.stderr}   
            return self.__run_results
        
        #When utility is still running over than timeout then test is failed
        except sp.TimeoutExpired:
            pytest.fail("Utility runtime is reached the timeout")
            self.__utility_ran.kill()
            #Tuple of captured things
            self.__run_results = {"ReturnCode": self.__utility_ran.returncode, 
                                  "STDOUT": self.__utility_ran.stdout, 
                                  "STDERR": self.__utility_ran.stderr}
            return self.__run_results
        