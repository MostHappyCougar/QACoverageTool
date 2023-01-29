# Description
Utility to perform coverage analysis for tests. This utility is applicable for xlsx documents with structure that correlate to the analysis mode (Detail mods description will be introduced in Wiki)

# How to install:
```
$ git clone https://github.com/MostHappyCougar/QACoverageTool.git
```
Or just download packages from last release

## Requirements
_requirements.txt_ file is in code/python directory of this utility.
Change current work directory to `some/path/to/code/python` then execute in terminal to install requirements: 
```
$ pip install -r requirements.txt
```
or
```
$ pip install -r path/to/requirements.txt
```
from any work directory.

# Usage
To use this utility you should run `cov_tool.py` as regular python script with any of following arguments means analysis mode:

### Example:
```
$ python cov_tool.py std
```

**At this moment there is only one mod**

1. `std` - state-transitions diagram
<details>
<summary>Usage Example - std</summary>

#### Configuration: 
Config file for this usage case is: `code/python/configurations/state_transitions_config.yaml`

#### Imput Table for analysis:
![image](https://user-images.githubusercontent.com/104580123/215318025-ba3d7ca3-8e6e-408c-86be-5dce72c41b4a.png)

#### Analysis results:
There is following files as result of analysis in `code/python/output/EXAMPLE`:
- test.gv - dot-language file for state-transitions diagram
```
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
- test.gv.pdf - state-treansitions diagram in pdf format

![image](https://user-images.githubusercontent.com/104580123/215318403-5b87cff6-a39e-46a2-bb1b-4beab25dbcee.png)
- test_stats.xlsx - detail **path** informations. There is no ways to representate **path** via state-transitions diagram so **path** will be descriped as text

![image](https://user-images.githubusercontent.com/104580123/215318691-b9729115-4a99-41fd-a6c8-6f836c607849.png)
- test_stats_vis.pdf - pie diagram that representate sequences of each path

![image](https://user-images.githubusercontent.com/104580123/215318768-4b751ef9-c1bc-45c4-8dd4-91628adac263.png)
</details>

## Configuration
Before script running you should configurate an analysis mode directly via related config stored in `code/python/configurations` (At this moment there is only one config for state-transitions diagram mode). Fields description is introduced in related config file. Also each config file is valid pre-configured for example files.
