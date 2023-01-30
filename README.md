# Description
Utility to perform coverage analysis for tests. This utility is applicable for xlsx documents with structure that correlate to the analysis mode

# How to install
```
$ git clone https://github.com/MostHappyCougar/QACoverageTool.git
```
Or just download packages from last release

## Requirements
`requirements.txt` file is in code/python directory of this utility.
Change current work directory to `some/path/to/code/python` then execute in terminal to install requirements: 
```
$ pip install -r requirements.txt
```
or
```
$ pip install -r path/to/requirements.txt
```
from any work directory

# Usage
To use this utility you should run `cov_tool.py` as regular python script with config name as an argument (without file extension). There may be several configs listed. All configs enumerated in arguments at `cov_tool.py` starts will be parsed and applied for tests coverage analysis. When no configs listed as agruments then `conf_default.yaml` will be applied. To chose analysis mods that will be aplied for tests you should enumerate them in `analysis-mods` section of `.yaml` config. There is the list of available analysis mods:

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
	
		<details><summary>test.gv - dot-language file for state-transitions diagram</summary>

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

		<details><summary>test.gv.pdf - state-treansitions diagram in pdf format</summary>

		![image](https://user-images.githubusercontent.com/104580123/215318403-5b87cff6-a39e-46a2-bb1b-4beab25dbcee.png)
		</details>

		<details><summary>test_stats.xlsx - detail path information</summary>

		![image](https://user-images.githubusercontent.com/104580123/215318691-b9729115-4a99-41fd-a6c8-6f836c607849.png)
		</details>
		<details><summary>test_stats_vis.pdf - pie diagram that representate sequences of each path</summary>

		![image](https://user-images.githubusercontent.com/104580123/215318768-4b751ef9-c1bc-45c4-8dd4-91628adac263.png)
		</details>
	</details>

#### Example: 
```
$ python cov_tool.py conf_default
```
