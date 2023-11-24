import os
import allure
import pytest
import time

from common_methods import user, files_processor
from common_methods import GLOBAL

@allure.parent_suite("2_Configurations")
@allure.suite("2_2_Run_Arguments")
@allure.sub_suite("2_2_2_Positive")
@allure.tag("positive", "configurations", "run_arguments")
@allure.feature("Configuration")
@allure.severity(allure.severity_level.TRIVIAL)
class TestPositive:
    '''
    There is exist an additional validation for list of configs with SEVERAL analysis mods and SINGLE analysis mod per list
    In onle config list exists two configs. One config contains a SINGLE analysis mod, another config contains SEVERAL analysis mods
    '''
    
    os.path.join("TEST", "conf_2_2_2_1")
    
    @pytest.mark.parametrize('case_id, run_arguments', [(None, [os.path.join("TEST", "conf_2_2_2_1"), os.path.join("TEST", "conf_2_2_2_2")]),
                                                        ("EXAMPLE", [])])
    def test_RunAgruments(self, case_id, run_arguments):
        
        #Output files list
        _output_files_list_first = ["2_2_2_Positive_path_stats_vis.pdf", "2_2_2_Positive_path_stats.xlsx", "2_2_2_Positive.gv", "2_2_2_Positive.gv.pdf"]
        _output_files_list_second = ["2_2_2_Positive_path_stats_vis.pdf", "2_2_2_Positive_path_stats.xlsx", "2_2_2_Positive.gv", "2_2_2_Positive.gv.pdf", "2_2_2_Positive_param_trace.xlsx"]
        _output_files_list_empty_config = ["EX_TEST_path_stats_vis.pdf", "EX_TEST_path_stats.xlsx", "EX_TEST.gv", "EX_TEST.gv.pdf", "EX_TEST_param_trace.xlsx"]
        
        #Path to output directory
        _path_to_out_f = os.path.join(GLOBAL.GLOBAL.path_from_test_to_util, "..", "output", "2_2_2_Positive", "case_1")
        _path_to_out_s = os.path.join(GLOBAL.GLOBAL.path_from_test_to_util, "..", "output", "2_2_2_Positive", "case_2")      
               
        with allure.step("Preconditions"):
            with allure.step("Flush output"):
                if case_id:
                    _out_files_empty = os.path.join(GLOBAL.GLOBAL.path_from_test_to_util, "..", "output", case_id)
                    _output_files_e = files_processor.OutputManager(_out_files_empty)
                    _output_files_e.delete_files(files=_output_files_list_empty_config)
                else:
                    _output_files_f = files_processor.OutputManager(_path_to_out_f)
                    _output_files_s = files_processor.OutputManager(_path_to_out_s) 
                    _output_files_f.delete_files(files=_output_files_list_first)
                    _output_files_s.delete_files(files=_output_files_list_second)
                
        with allure.step("Run utility"):
            _actual_artifacts = user.User().try_to_get_exit_artifacts(run_arguments)
            print(_actual_artifacts["STDERR"].decode('utf-8', errors='ignore'))

        with allure.step("Postconditions"):
                time.sleep(1)
                with allure.step("Flush output files and validate if there was generated"):
                    if run_arguments:
                        with allure.step("Output of FIRST config"):
                            _output_files_f.delete_files(files=_output_files_list_first, fail_if_absence=True)
                        with allure.step("Output of SECOND config"):
                            _output_files_s.delete_files(files=_output_files_list_second, fail_if_absence=True)
                    else:
                        with allure.step("Empty Config"):
                            _output_files_e.delete_files(files=_output_files_list_empty_config, fail_if_absence=True)

                        

            
        
                
                
                
                
                
                