import os

import graphviz as gv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from analysis import AAnalysis
from save_data import ISaveData
from input_adapter_std import InputAdapter


class StateTransitionsDiagram(AAnalysis, ISaveData):
    '''
    Base class for State-Transitions Diagram analysis mod
    '''
    
    def __init__(self, config: dict):
        super().__init__(config, InputAdapter)
        
        #Read related config fields
        self.output_directory = os.path.join(os.path.dirname(__file__), "output", self.mod_params["output_directory"])
        
        #Get dataframe for analysis and sort it out based on OBJECTS and SEQUENCES fields
        self.sorted = self.dataframe.sort_values([*self.mod_params["objects"], *self.mod_params["sequences"]])
        self.transformed = pd.DataFrame(columns=["seq", "object", "transitions", "states"])
        
        #State-Transitions Graph building
        self.graph = gv.Digraph(name=self.mod_params["file_names"], graph_attr={"concentrate":"true", "imagescale": "true"}, strict=True)
        self.graph.node("START", "START", fontcolor="white", fillcolor="red", style="filled")
        self.graph.node("END", "END", fontcolor="white", fillcolor="red", style="filled")
        
        #This fields will be used for build path statistics
        self.path_list = []
        self.path_dataframe = pd.DataFrame(columns=["path"])
        self.path_stats = pd.DataFrame(columns=["PathID", "Path", "Count"])
        
        #Lists for unique entities to iterate states and transitions
        self.objects_unique = self.transformed["object"].unique()
        self.states_unique = self.transformed["states"].unique()
        self.transitions_unique = self.transformed["transitions"].unique()
        
         
    def save_results(self) -> None:
        '''
        Save analysis results
        '''
        
        self.graph.render(directory=f"{self.output_directory}", view=False)
        
        with pd.ExcelWriter(f"{os.path.join(self.output_directory, self.mod_params['file_names'])}_path_stats.xlsx") as writer:
            self.transition_statistics.to_excel(writer, "PathStatistics")

        fig, (ax1) = plt.subplots()
        ax1.set(title="Path frequency by PathID")
        ax1.pie(x=self.transition_statistics["Count"], labels=self.transition_statistics.index, autopct='%1.1f%%')
        plt.savefig(f"{os.path.join(self.output_directory, self.mod_params['file_names'])}_path_stats_vis.pdf")

    
    def analyse(self) -> None:
        '''
        State-Transitions analysis execution.
        This method calls another following methods in following order:
        
        _transform_dateframe_before_analysis
        _build_graph
        _path_statistics_gen
        save_results
        '''
        
        self._transform_dateframe_before_analysis() 
        self._build_graph()
        self._path_statistics_generation()
        self.save_results()
        
        print(f"\nStates-transitions analysys has been succesfully performed. Actifacts saved upon: {self.output_directory}")
        
        
    def _build_graph(self):
        '''
        Method for Graph building
        '''
        
        for obj in self.objects_unique:
            #Foreach object build path
            object_path = [row for row in self.transformed.itertuples(index=False, name=None) if obj == row[1]]
            self.path_list.append(np.array(object_path)[:, 2:])
            
            #Build graph based on pass
            self.graph.edge("START", object_path[0][3], object_path[0][2])
            for state in range(len(object_path)):
                try:
                    self.graph.edge(object_path[state][3], object_path[state+1][3], object_path[state+1][2])
                except:
                    self.graph.edge(object_path[state][3], "END")
                    
                    
    def _path_statistics_generation(self):
        '''
        Collect and processing path statistics
        '''
        
        #Make dataframe of path. No bound to any object will be considered.
        #It is required to collect path statistics
        for path in self.path_list:
            self.listed_path = pd.DataFrame([[path]], columns=["path"])
            self.path_dataframe = pd.concat([self.path_dataframe, self.listed_path]).astype(str)
        
        #Make path statistics
        self.transition_statistics = pd.DataFrame(np.c_[np.unique(self.path_dataframe, return_counts=1)], columns=["Path", "Count"])
        self.transition_statistics.index.name = "PathID" 
        
    
    def _transform_dateframe_before_analysis(self) -> None:
        '''
        Input dataframe transformation. 
        As per several columns might be specified for any parameter (sequencer, object, teansitions, states)
        list of all values of enlisted columns must be considered as single instance per dataframe index foreach parameter
        '''
        
        #Transform dataframe according to the required structure
        self.transformed["seq"] = self.sorted[self.mod_params["sequences"]].astype(str).apply(", ".join, axis=1)
        self.transformed["object"] = self.sorted[self.mod_params["objects"]].astype(str).apply(", ".join, axis=1)
        self.transformed["transitions"] = self.sorted[self.mod_params["transitions"]].astype(str).apply(", ".join, axis=1)
        self.transformed["states"] = self.sorted[self.mod_params["states"]].astype(str).apply(", ".join, axis=1)
        
        #Lists for unique entities to iterate states and transitions
        self.objects_unique = self.transformed["object"].unique()
        self.states_unique = self.transformed["states"].unique()
        self.transitions_unique = self.transformed["transitions"].unique()
        
        
        
        