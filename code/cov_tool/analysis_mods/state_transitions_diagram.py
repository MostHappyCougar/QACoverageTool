import os

import graphviz as gv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from abstractions.analysis import AAnalysis
from abstractions.save_data import ISaveData
from input_sockets.input_socket_std import InputSocket


class StateTransitionsDiagram(AAnalysis, ISaveData):
    '''
    Base class for State-Transitions Diagram analysis mod
    '''
    
    def __init__(self, mod_params: dict):
        super().__init__(mod_params, InputSocket)
        
        self._output_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "output", self._mod_params["output_directory"]))
        
        self._sorted = self._dataframe.sort_values([*self._mod_params["objects"], *self._mod_params["sequences"]])
        self._transformed = pd.DataFrame(columns=["seq", "object", "transitions", "states"])
        
        #Common Graph Nodes
        self._graph = gv.Digraph(name=self._mod_params["file_names"], graph_attr={"concentrate":"true", "imagescale": "true"}, strict=True)
        self._graph.node("START", "START", fontcolor="white", fillcolor="red", style="filled")
        self._graph.node("END", "END", fontcolor="white", fillcolor="red", style="filled")
        
        #This fiels will be used for building PATH STATISTICS
        self._path_list = []
        self._path_dataframe = pd.DataFrame(columns=["path"])
        self._path_stats = pd.DataFrame(columns=["PathID", "Path", "Count"])
        
        self._objects_unique = self._transformed["object"].unique()
        self._states_unique = self._transformed["states"].unique()
        self._transitions_unique = self._transformed["transitions"].unique()
        

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
        
        print(f"\nStates-transitions analysys has been succesfully performed. Actifacts saved upon: {self._output_directory}")
        
        
    def _transform_dateframe_before_analysis(self) -> None:
        '''
        Input dataframe transformation. 
        As per several columns might be specified for any parameter (sequencer, object, teansitions, states)
        list of all values of enlisted columns must be considered as single instance per dataframe index foreach parameter
        '''
        
        self._transformed["seq"] = self._sorted[self._mod_params["sequences"]].astype(str).apply(", ".join, axis=1)
        self._transformed["object"] = self._sorted[self._mod_params["objects"]].astype(str).apply(", ".join, axis=1)
        self._transformed["transitions"] = self._sorted[self._mod_params["transitions"]].astype(str).apply(", ".join, axis=1)
        self._transformed["states"] = self._sorted[self._mod_params["states"]].astype(str).apply(", ".join, axis=1)
        
        self._objects_unique = self._transformed["object"].unique()
        self._states_unique = self._transformed["states"].unique()
        self._transitions_unique = self._transformed["transitions"].unique()
        
        
    def _build_graph(self):
        for obj in self._objects_unique:
            object_path = self._group_states_by_object(obj)
            
            #It is required to further PATH STATISTICS building
            self._append_path_list(object_path)
            
            self._graph.edge("START", object_path[0][3], object_path[0][2])
            for state in range(len(object_path)):
                try:
                    self._graph.edge(object_path[state][3], object_path[state+1][3], object_path[state+1][2])
                except IndexError:
                    self._graph.edge(object_path[state][3], "END")
        
                    
    def _group_states_by_object(self, object_id: str) -> list[list]:
        return [row for row in self._transformed.itertuples(index=False, name=None) if object_id == row[1]]
    
    
    def _append_path_list(self, object_path: list[list]) -> None:
        self._path_list.append(np.array(object_path)[:, 2:])
                    
                    
    def _path_statistics_generation(self):        
        self._make_dataframe_from_path_list()
        
        self._path_stats = pd.DataFrame(np.c_[np.unique(self._path_dataframe, return_counts=1)], columns=["Path", "Count"])
        self._path_stats.index.name = "PathID" 
        
        
    def _make_dataframe_from_path_list(self) -> None:
        for path in self._path_list:
            self._listed_path = pd.DataFrame([[path]], columns=["path"])
            self._path_dataframe = pd.concat([self._path_dataframe, self._listed_path]).astype(str)
        
    
    def save_results(self) -> None:        
        self._graph.render(directory=f"{self._output_directory}", view=False)
        
        with pd.ExcelWriter(f"{os.path.join(self._output_directory, self._mod_params['file_names'])}_path_stats.xlsx") as writer:
            self._path_stats.to_excel(writer, "PathStatistics")

        fig, (ax1) = plt.subplots()
        ax1.set(title="Path frequency by PathID")
        ax1.pie(x=self._path_stats["Count"], labels=self._path_stats.index, autopct='%1.1f%%')
        plt.savefig(f"{os.path.join(self._output_directory, self._mod_params['file_names'])}_path_stats_vis.pdf")
        
        
        
        