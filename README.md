### PROD status
[![Regression Testing UBUNTU](https://github.com/MostHappyCougar/QACoverageTool/actions/workflows/regression-ubuntu.yml/badge.svg?branch=prod)](https://github.com/MostHappyCougar/QACoverageTool/actions/workflows/regression-ubuntu.yml)
[![Regression Testing WINDOWS](https://github.com/MostHappyCougar/QACoverageTool/actions/workflows/regression-windows.yml/badge.svg?branch=prod)](https://github.com/MostHappyCougar/QACoverageTool/actions/workflows/regression-windows.yml)
[![CodeQL](https://github.com/MostHappyCougar/QACoverageTool/actions/workflows/codeql.yml/badge.svg?branch=prod)](https://github.com/MostHappyCougar/QACoverageTool/actions/workflows/codeql.yml)
![GitHub](https://img.shields.io/github/license/MostHappyCougar/QACoverageTool?label=Licence)
[![CodeFactor](https://www.codefactor.io/repository/github/mosthappycougar/qacoveragetool/badge)](https://www.codefactor.io/repository/github/mosthappycougar/qacoveragetool)
# Description
Utility to perform tests coverage analysis based on `xlsx` tables e.g scenarios, test cases or download of system states. This utility is applicable for documents with structure that correlate to the analysis mode. 

[To see more details please visit Wiki](https://github.com/MostHappyCougar/QACoverageTool/wiki)

# How to install
```
$ git clone https://github.com/MostHappyCougar/QACoverageTool.git
```
Or just download packages from last release

## Requirements
`requirements.txt` file is in code/python directory of this utility.
Change current work directory to `some/path/to/code/cov_tool` then execute in terminal to install requirements: 
```
$ pip install -r requirements.txt
```
or
```
$ pip install -r path/to/requirements.txt
```
from any work directory

# Usage
## Configuration
Befure utility use you should create and configure a config in `/code/configurations/` directory. There is should be specified a list of analysis mods that will be performed at utility run. Also you can configure each analysis mod in details via mentioned config. There is possible to store several configs and use any count of them individually or together

<details><summary>Config Example</summary>

### This config is prepared for EXAMPLE.xlsx and 1_2_1_TEST.xlsx stored in `code/tables_to_analisys/`

```yaml
##############################################
#ANALYSIS MODS THAT WILL BE APPLIED FOR TESTS#
#                                            #
#Applicable mods:                            #
# - state-transitions                        #
# - parameters-traceability                  #
##############################################
analysis-mods:
   - state-transition
   - parameters-traceability


#########################################
#DETAIL CONFIGURATIONS FOR ANALYSIS MODS#
#########################################

#State-transitions diagram
state-transition:
   #All generated files will be saved here.
   output_directory: EXAMPLE
   file_names: EX_TEST
   #Table and sheet where data to analysis will be take from
   input_directory: tables_to_analisys
   input_table: EXAMPLE.xlsx
   input_sheet: test

   #States and transitions will be assigned to object based on these table columns.
   #When values from objects columns is same for several states/transitions then these states/transitions will be related to this object
   #You may mention here a several columns. So each unique compination of values of mentioned columns will be considered as one unique object
   objects:
      - TestCase

   #Sequence of transitions and states will be considered based on this field
   sequences:
      - StepID

   #Transitions will be took from these fields
   #You may mention here a several columns. Each unique combination of values of mentioned columns will be considered as one transition
   transitions:
      - Action

   #States will be took from these fields
   #You may mention here a several columns. Each unique combination of values from mentioned columns will be considered as one state
   states:
      - CountToPlace
      - CountToCancel

parameters-traceability:
   #All generated files will be saved here.
   output_directory: EXAMPLE
   file_names: EX_TEST
   #Table and sheet where data to analysis will be take from
   input_directory: tables_to_analisys
   input_table: TEST/1_2_1_TEST.xlsx
   input_sheet: Cases

   index:
      - Sequencer
      - Object

   columns:
      - Transitions
      - States
```

</details>

## Running
To use this utility you should run `cov_tool` that placed in `/code/` directory of this utility with config name as an argument (without file extension). There may be several configs listed. All configs enumerated in arguments at `cov_tool` starts will be parsed and applied for tests coverage analysis. When no configs listed as agruments then `conf_default.yaml` will be applied. **This config is valid preconfigured for example files.** To chose analysis mods that will be aplied for tests you should enumerate them in `analysis-mods` section of `.yaml` config.
#### Example: 
```
$ python cov_tool conf_default
```

## Analysis mods
1. `state-transition` - state-transitions diagram
	```yaml
	analysis-mods:
	   - state-transition
	```
	<details><summary>Usage Example - state-transition</summary>
	
	#### Preconditions:
	- Configuration: 
	
		Config file for this usage case is: `code/python/configurations/conf_default.yaml`

	- Input table for analysis - there is should be no merged cells:
		
		<details><summary>Table to analysis</summary>

		![image](https://user-images.githubusercontent.com/104580123/215318025-ba3d7ca3-8e6e-408c-86be-5dce72c41b4a.png)
		</details>

	#### Analysis results:
	- There is following files as result of analysis in `code/python/output/EXAMPLE`:
	
		<details><summary>EX_TEST.gv - dot-language file for state-transitions diagram</summary>

		```dot
		strict digraph "D:\Dev_Workspace\Eclipse\QACoverageTool\code\python\output\EXAMPLE\test" {
			graph [concentrate=true imagescale=true]
			START [label=START fillcolor=red fontcolor=white style=filled]
			END [label=END fillcolor=red fontcolor=white style=filled]
			START -> "3, 0" [label=place]
			"3, 0" -> "0, 2" [label=cancel]
			"0, 2" -> "3, 0" [label=place]
			"3, 0" -> END
			START -> "3, 0" [label=place]
			"3, 0" -> "0, 1" [label=cancel]
			"0, 1" -> "3, 0" [label=place]
			"3, 0" -> END
			START -> "3, 0" [label=place]
			"3, 0" -> "0, 4" [label=cancel]
			"0, 4" -> "3, 0" [label=place]
			"3, 0" -> END
			START -> "3, 0" [label=place]
			"3, 0" -> "0, 2" [label=cancel]
			"0, 2" -> "3, 0" [label=place]
			"3, 0" -> END
			START -> "3, 0" [label=place]
			"3, 0" -> "0, 4" [label=cancel]
			"0, 4" -> "3, 0" [label=place]
			"3, 0" -> END
			START -> "3, 0" [label=place]
			"3, 0" -> "0, 3" [label=cancel]
			"0, 3" -> "3, 0" [label=place]
			"3, 0" -> END
			START -> "3, 0" [label=place]
			"3, 0" -> "0, 3" [label=cancel]
			"0, 3" -> "3, 0" [label=place]
			"3, 0" -> END
			START -> "3, 0" [label=place]
			"3, 0" -> "0, 4" [label=cancel]
			"0, 4" -> "3, 0" [label=place]
			"3, 0" -> END
			START -> "3, 0" [label=place]
			"3, 0" -> "0, 1" [label=cancel]
			"0, 1" -> "3, 0" [label=place]
			"3, 0" -> END
			START -> "3, 0" [label=place]
			"3, 0" -> "0, 3" [label=cancel]
			"0, 3" -> "3, 0" [label=place]
			"3, 0" -> END
			START -> "3, 0" [label=place]
			"3, 0" -> "0, 2" [label=cancel]
			"0, 2" -> "3, 0" [label=place]
			"3, 0" -> END
			START -> "3, 0" [label=place]
			"3, 0" -> "0, 1" [label=cancel]
			"0, 1" -> "3, 0" [label=place]
			"3, 0" -> END
		}
		```
		</details>

		<details><summary>EX_TEST.gv.pdf - state-treansitions diagram in pdf format</summary>

		![image](https://user-images.githubusercontent.com/104580123/215318403-5b87cff6-a39e-46a2-bb1b-4beab25dbcee.png)
		</details>

		<details><summary>EX_TEST_path_stats.xlsx - detail path information</summary>

		![image](https://user-images.githubusercontent.com/104580123/215318691-b9729115-4a99-41fd-a6c8-6f836c607849.png)
		</details>
		<details><summary>EX_TEST_path_stats_vis.pdf - pie diagram that representate sequences of each path</summary>

		![image](https://user-images.githubusercontent.com/104580123/215318768-4b751ef9-c1bc-45c4-8dd4-91628adac263.png)
		</details>
	</details>
2. `parameters-traceability` - parameters traceability matrix
	```yaml
	analysis-mods:
	   - parameters-traceability
	```
	<details><summary>Usage Example - parameters-traceability</summary>
	
	#### Preconditions:
	- Configuration: 
	
		Config file for this usage case is: `code/python/configurations/conf_default.yaml`

	- Input table for analysis - there is should be no merged cells:
		
		<details><summary>Table to analysis</summary>

		![image](https://user-images.githubusercontent.com/104580123/219852038-aa353e96-3097-4be6-830c-6e069b4afd57.png)

		</details>
		
	#### Analysis results:
	- There is following files as result of analysis in `code/python/output/EXAMPLE`:
	
		<details><summary>EX_TEST_param_trace.xlsx</summary>
		
		![image](https://user-images.githubusercontent.com/104580123/219852225-f764875a-e920-4048-ad58-344cc37af1c0.png)
		
		</details>
	</details>
