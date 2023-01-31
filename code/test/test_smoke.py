from common_methods import user_actions, output_manager, read_global
import os
import allure

@allure.parent_suite("0_SMOKE")
@allure.suite("0_0_State-Transitions_Diagram")
@allure.sub_suite("0_0_0_Single_Config")
@allure.tag("smoke", "state-transition", "positive")
class TestSmoke():
    def test_smoke(self) -> None:
        #Get global parameters for this test
        _global_parameters = read_global.GlobalConfig()
        #spected rtifacts at utility execution complete
        _expected_artifacts = output_manager.ExpectedSTDMessages()
        #actual artifats at utility copmplete
        _relative_path_to_expected_files = os.path.join(_global_parameters.get_params()["relative_path"]["from_test_to_expected"], "SMOKE")
        #Expected output files
        _expected_output_files = output_manager.FilesManagement(_relative_path_to_expected_files)
        
        with allure.step("Preconditions"):
            with allure.step("Flush output"): 
                #Output files at utility complete
                _path_to_output_files = os.path.join(_global_parameters.get_params()["relative_path"]["from_test_to_utility"], "output", "EXAMPLE")
                #Output files
                _output_files = output_manager.FilesManagement(_path_to_output_files)
                _output_files.remove_files(files=["test_stats_vis.pdf", "test_stats.xlsx", "test.gv", "test.gv.pdf"])
        
        with allure.step("Run utility"):
            _actual_artifacts = user_actions.User().try_to_run()
            
        with allure.step("Validations"):
            with allure.step("Artifacts"):
                with allure.step("Return Code"):
                    assert 0 == _actual_artifacts["ReturnCode"]
                with allure.step("STDOUT"):
                    assert _expected_artifacts.read()["stdout"]["SMOKE"] == _actual_artifacts["STDOUT"].decode()
                with allure.step("STDERR"):
                    assert _expected_artifacts.read()["stderr"]["SMOKE"] == _actual_artifacts["STDERR"].decode()
            with allure.step("Output Files"):
                for file in ["test.gv"]:
                    with allure.step(f"Compare {file}"):
                        assert _expected_output_files.read_file(file) == _output_files.read_file(file)
        
        
        