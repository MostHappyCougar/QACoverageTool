from common_methods import user_actions, output_manager, read_global
import os
import allure
import pytest
import pandas as pd

@allure.parent_suite("1_Analysis_Mods")
@allure.suite("1_1_State-Transitions_Diagram")
@allure.sub_suite("1_1_1_Positive")
@allure.tag("positive", "state-transitions", "analysis_mods")
@allure.feature("State-Transitions Diagram")
@allure.severity(allure.severity_level.CRITICAL)
class TestStateTransitions():
    
    @pytest.mark.parametrize("config, expected_files", [("TEST/std_case_1", "std_case1"),
                                                        ("TEST/std_case_2", "std_case2"),
                                                        ("TEST/std_case_3", "std_case3"),
                                                        ("TEST/std_case_4", "std_case4"),
                                                        ("TEST/std_case_5", "std_case5")])
    def test_StateTransitions(self, config, expected_files) -> None:
        #The list of expected files at the utility execution complete
        _output_files_list = ["1_1_1_Positive_stats_vis.pdf", "1_1_1_Positive_stats.xlsx", "1_1_1_Positive.gv", "1_1_1_Positive.gv.pdf"]
        
        #Get global parameters for this test
        _global_parameters = read_global.GlobalConfig()
        
        #Spected rtifacts at utility execution complete
        _expected_artifacts = output_manager.ExpectedSTDMessages()
        
        #Expected output files
        _relative_path_to_expected_files = os.path.join(_global_parameters.get_params()["relative_path"]["from_test_to_expected"], expected_files)
        _expected_output_files = output_manager.FilesManagement(_relative_path_to_expected_files)
        
        #Actual output files
        _path_to_output_files = os.path.join(_global_parameters.get_params()["relative_path"]["from_test_to_utility"], "output", "1_1_1_Positive")
        _output_files = output_manager.FilesManagement(_path_to_output_files)
        
        with allure.step("Preconditions"):
            with allure.step("Flush output"): 
                
                #Output files remove
                _output_files.remove_files(files=_output_files_list)
        
        with allure.step("Run utility"):
            _actual_artifacts = user_actions.User().try_to_run(config)
            
        try:
            with allure.step("Validations"):
                with allure.step("Artifacts"):
                    with allure.step("Return Code"):
                        assert 0 == _actual_artifacts["ReturnCode"]
                    #with allure.step("STDOUT"):
                        #assert _expected_artifacts.read()["stdout"]["positive_1_1_1"] == _actual_artifacts["STDOUT"].decode()
                    with allure.step("STDERR"):
                        assert _expected_artifacts.read()["stderr"]["positive_1_1_1"] == _actual_artifacts["STDERR"].decode()
                with allure.step("Output Files"):
                    for file in ["1_1_1_Positive.gv"]:
                        with allure.step(f"Compare {file}"):
                            assert _expected_output_files.read_file(file) == _output_files.read_file(file)
                    with allure.step("Compare 1_1_1_Positive_stats.xlsx"):
                        assert True == _expected_output_files.read_table("1_1_1_Positive_stats.xlsx").compare(_output_files.read_table("1_1_1_Positive_stats.xlsx")).empty
        finally:
            with allure.step("Postconditions"):
                with allure.step("Flush output files and validate if there was generated"):
                    _output_files.remove_files(files=_output_files_list, validate=True)
        
        
        