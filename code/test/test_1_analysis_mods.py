'''
There is code duplication because two different cases may be changed separately and irrespective to each other
'''

import os
import allure
import pytest
import sys
import codecs

from common_methods import user, files_processor
from common_methods import GLOBAL

@allure.parent_suite("1_Analysis_Mods")
@allure.suite("1_1_State-Transitions_Diagram")
@allure.sub_suite("1_1_1_Positive")
@allure.tag("positive", "state-transitions", "analysis_mods")
@allure.feature("State-Transitions Diagram")
@allure.severity(allure.severity_level.CRITICAL)
class TestStateTransitions():
    
    @pytest.mark.parametrize("config, expected_files", [([os.path.join("TEST", "std_case_1")], "std_case1"),
                                                        ([os.path.join("TEST", "std_case_2")], "std_case2"),
                                                        ([os.path.join("TEST", "std_case_3")], "std_case3"),
                                                        ([os.path.join("TEST", "std_case_4")], "std_case4"),
                                                        ([os.path.join("TEST", "std_case_5")], "std_case5")])
    def test_StateTransitions(self, config, expected_files) -> None:

        output_files = ["1_1_1_Positive_path_stats_vis.pdf", "1_1_1_Positive_path_stats.xlsx", "1_1_1_Positive.gv", "1_1_1_Positive.gv.pdf"] 
        path_to_enter_point = os.path.abspath(os.path.join(GLOBAL.GLOBAL.path_from_test_to_util))
        path_to_actual_output = os.path.abspath(os.path.join(path_to_enter_point, "..", "code", "output", "1_1_1_Positive"))
        path_to_expected_output = os.path.join(GLOBAL.GLOBAL.path_from_test_to_expected, expected_files)
        path_to_expected_std = os.path.join(GLOBAL.GLOBAL.path_from_test_to_expected, "..")
        
        usr = user.User()
        
        out_manager_act = files_processor.OutputManager(path_to_actual_output)
        bin_reader_act = files_processor.BinaryReader(path_to_actual_output)
        xlsx_reader_act = files_processor.XLSXReader(path_to_actual_output)
        
        bin_reader_exp = files_processor.BinaryReader(path_to_expected_output)
        xlsx_reader_exp = files_processor.XLSXReader(path_to_expected_output)
        std_exp = files_processor.YAMLReader(path_to_expected_std)
        
        
        with allure.step("Preconditions"):
            with allure.step("Flush Output Directory"):
                out_manager_act.delete_files(files=output_files, fail_if_absence=False)
                
        
        with allure.step("Run Utility"):
            actual_artifacts = usr.try_to_get_exit_artifacts(arguments=config)
        
        
        try: 
            with allure.step("Validations"):
                with allure.step("Artifacts"):
                    with allure.step("Exit Code"):
                        #print(codecs.decode(actual_artifacts["STDERR"], encoding='unicode_escape'))
                        assert 0 == actual_artifacts["ReturnCode"]
                    with allure.step("STDOUT"):
                        expected_stdout = '\n'+std_exp.read_file("std.yml")["stdout"]["positive_1_1_1"]+path_to_actual_output+'\n'
                        #assert expected_stdout.replace('\r', '') == codecs.decode(actual_artifacts["STDOUT"], encoding='unicode_escape').replace('\r', '')
                    with allure.step("STDERR"):
                        mpl_err = "Matplotlib is building the font cache; this may take a moment."+'\n'
                        #assert '' == codecs.decode(actual_artifacts["STDERR"], encoding='unicode_escape') or mpl_err == codecs.decode(actual_artifacts["STDERR"], encoding='unicode_escape').replace('\r', '')
                
                with allure.step("Output Files"):
                    with allure.step(output_files[2]):
                        assert bin_reader_exp.read_file(file=output_files[2]) == bin_reader_act.read_file(file=output_files[2])
                    with allure.step(output_files[1]):
                        assert True == xlsx_reader_exp.read_file(file=output_files[1]).compare(xlsx_reader_act.read_file(file=output_files[1])).empty
        finally:
            with allure.step("Postconditions"):
                with allure.step("Flush Output Files"):
                    out_manager_act.delete_files(files=output_files, fail_if_absence=True)
                    
                    

@allure.parent_suite("1_Analysis_Mods")
@allure.suite("1_2_Traceability_Matrix")
@allure.sub_suite("1_2_1_Positive")
@allure.tag("positive", "traceability_matrix", "analysis_mods")
@allure.feature("Traceability Matrix")
@allure.severity(allure.severity_level.CRITICAL)
class TestTraceabilityMatrix():
    
    @pytest.mark.parametrize("config, expected_files", [([os.path.join("TEST", "tm_case_1")], "tm_case1"),
                                                        ([os.path.join("TEST", "tm_case_2")], "tm_case2"),
                                                        ([os.path.join("TEST", "tm_case_3")], "tm_case3"),
                                                        ([os.path.join("TEST", "tm_case_4")], "tm_case4")])
    def test_TraceabilityMatrix(self, config, expected_files) -> None:

        output_files = ["1_2_1_Positive_param_trace.xlsx"] 
        path_to_enter_point = os.path.abspath(os.path.join(GLOBAL.GLOBAL.path_from_test_to_util))
        path_to_actual_output = os.path.abspath(os.path.join(path_to_enter_point, "..", "code", "output", "1_2_1_Positive"))
        path_to_expected_output = os.path.join(GLOBAL.GLOBAL.path_from_test_to_expected, expected_files)
        path_to_expected_std = os.path.join(GLOBAL.GLOBAL.path_from_test_to_expected, "..")
        
        usr = user.User()
        
        out_manager_act = files_processor.OutputManager(path_to_actual_output)
        xlsx_reader_act = files_processor.XLSXReader(path_to_actual_output)
        
        xlsx_reader_exp = files_processor.XLSXReader(path_to_expected_output)
        std_exp = files_processor.YAMLReader(path_to_expected_std)
        
        
        with allure.step("Preconditions"):
            with allure.step("Flush Output Directory"):
                out_manager_act.delete_files(files=output_files, fail_if_absence=False)
                
        
        with allure.step("Run Utility"):
            actual_artifacts = usr.try_to_get_exit_artifacts(arguments=config)
        
        
        try: 
            with allure.step("Validations"):
                with allure.step("Artifacts"):
                    with allure.step("Exit Code"):
                        #print(codecs.decode(actual_artifacts["STDERR"], encoding='unicode_escape'))
                        assert 0 == actual_artifacts["ReturnCode"]
                    with allure.step("STDOUT"):
                        expected_stdout = '\n'+std_exp.read_file("std.yml")["stdout"]["positive_1_2_1"]+path_to_actual_output+'\n'
                        #assert expected_stdout.replace('\r', '') == codecs.decode(actual_artifacts["STDOUT"], encoding='unicode_escape').replace('\r', '')
                    with allure.step("STDERR"):
                        mpl_err = "Matplotlib is building the font cache; this may take a moment."+'\n'
                        #assert '' == actual_artifacts["STDERR"] or mpl_err == codecs.decode(actual_artifacts["STDERR"], encoding='unicode_escape').replace('\r', '')
                
                with allure.step("Output Files"):
                    with allure.step(output_files[0]):
                        assert True == xlsx_reader_exp.read_file(file=output_files[0]).compare(xlsx_reader_act.read_file(file=output_files[0])).empty
        finally:
            with allure.step("Postconditions"):
                with allure.step("Flush Output Files"):
                    out_manager_act.delete_files(files=output_files, fail_if_absence=True)
            
        
        
        
        
