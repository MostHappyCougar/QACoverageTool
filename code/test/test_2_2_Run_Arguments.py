import os
import allure
import pytest
import time

from common_methods import user_actions, output_manager
from common_methods import GLOBAL

@allure.parent_suite("2_Configurations")
@allure.suite("2_2_Run_Arguments")
@allure.sub_suite("2_2_2_Positive")
@allure.tag("positive", "configurations", "run_arguments")
@allure.feature("Configuration")
@allure.severity(allure.severity_level.TRIVIAL)
class TestPositive:
    
    os.path.join("TEST", "conf_2_2_2_1")
    
    @pytest.mark.parametrize('case_id, run_arguments', [(None, [os.path.join("TEST", "conf_2_2_2_1"), os.path.join("TEST", "conf_2_2_2_2")]),
                                                        ("EXAMPLE", [])])
    def test_RunAgruments(self, case_id, run_arguments):
        
        #Output files list
        _output_files_list = ["2_2_2_Positive_path_stats_vis.pdf", "2_2_2_Positive_path_stats.xlsx", "2_2_2_Positive.gv", "2_2_2_Positive.gv.pdf"]
        _output_files_list_empty_config = ["EX_TEST_path_stats_vis.pdf", "EX_TEST_path_stats.xlsx", "EX_TEST.gv", "EX_TEST.gv.pdf"]
        
        #Path to output directory
        _path_to_out_f = os.path.join(GLOBAL.GLOBAL.path_from_test_to_util, "output", "2_2_2_Positive", "case_1")
        _path_to_out_s = os.path.join(GLOBAL.GLOBAL.path_from_test_to_util, "output", "2_2_2_Positive", "case_2")      
               
        with allure.step("Preconditions"):
            with allure.step("Flush output"):
                if case_id:
                    _out_files_empty = os.path.join(GLOBAL.GLOBAL.path_from_test_to_util, "output", case_id)
                    _output_files_e = output_manager.FilesManagement(_out_files_empty)
                    _output_files_e.remove_files(files=_output_files_list)
                else:
                    _output_files_f = output_manager.FilesManagement(_path_to_out_f)
                    _output_files_s = output_manager.FilesManagement(_path_to_out_s) 
                    _output_files_f.remove_files(files=_output_files_list)
                    _output_files_s.remove_files(files=_output_files_list)
                
        with allure.step("Run utility"):
            _actual_artifacts = user_actions.User().try_to_run(run_arguments)
            print(_actual_artifacts["STDERR"].decode())

        with allure.step("Postconditions"):
                time.sleep(1)
                with allure.step("Flush output files and validate if there was generated"):
                    if run_arguments:
                        with allure.step("Output of FIRST config"):
                            _output_files_f.remove_files(files=_output_files_list, validate=True)
                        with allure.step("Output of SECOND config"):
                            _output_files_s.remove_files(files=_output_files_list, validate=True)
                    else:
                        with allure.step("Empty Config"):
                            _output_files_e.remove_files(files=_output_files_list_empty_config, validate=True)

                        

            
        
                
                
                
                
                
                