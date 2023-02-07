import os

import graphviz as gv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from analysis import Analysis
from save_data import ISaveData
from input_adapter_std import InputAdapter


class StateTransitionsDiagram(Analysis, ISaveData):
    '''
    Realisation of Analysis abstraction for State-Transition Diagrams mod
    '''
    
    def __init__(self, config):
        self.config_parsed = config["state-transition"]
        self.output_directory = os.path.join(os.path.dirname(__file__), self.config_parsed["output_directory"])
        
                
    def save_results(self) -> None:
        '''
        Save analysis results
        '''
        self.graph.render(directory=f"{self.output_directory}", view=False)
        
        with pd.ExcelWriter(f"{os.path.join(self.output_directory, self.config_parsed['file_names'])}_stats.xlsx") as writer:
            self.trans_stat.to_excel(writer, "TransitionsStatistics")

        fig, (ax1) = plt.subplots()
        ax1.set(title="Transition frequency by TransitionID")
        ax1.pie(x=self.trans_stat["Count"], labels=self.trans_stat.index, autopct='%1.1f%%')
        plt.savefig(f"{os.path.join(self.output_directory, self.config_parsed['file_names'])}_stats_vis.pdf")

    
    def analyse(self) -> None:
        '''
        Realisation of analysis method of Analysis abstract class for State-Transitions Diagram mod
        '''
        
        self.dataframe = InputAdapter.DATAFRAME
        
        self.sorted_dataframe = self.dataframe.sort_values([*self.config_parsed["objects"], *self.config_parsed["sequences"]])
        self.aggregated_table = pd.DataFrame(columns=["seq", "object", "transitions", "states"])
        
        #Make aggregated dataframe from raw sorted input. 
        #To consider multiparametrized states we should add list of values foreach parameters list per dataframe index
        self.aggregated_table["seq"] = self.sorted_dataframe[self.config_parsed["sequences"]].astype(str).apply(", ".join, axis=1)
        self.aggregated_table["object"] = self.sorted_dataframe[self.config_parsed["objects"]].astype(str).apply(", ".join, axis=1)
        self.aggregated_table["transitions"] = self.sorted_dataframe[self.config_parsed["transitions"]].astype(str).apply(", ".join, axis=1)
        self.aggregated_table["states"] = self.sorted_dataframe[self.config_parsed["states"]].astype(str).apply(", ".join, axis=1)
        
        #This fields will be used for build path statistics
        self.transitions_list = []
        self.transitions_dataframe = pd.DataFrame(columns=["transitions"])
        self.stransitions_stats = pd.DataFrame(columns=["TransitionID", "Transition", "Count"])
        
        #Lists for unique entities to iterate states and transitions
        self.objects = self.aggregated_table["object"].unique()
        self.states = self.aggregated_table["states"].unique()
        self.transitions = self.aggregated_table["transitions"].unique()
        
        #State-Transitions Graph building
        self.graph = gv.Digraph(name=self.config_parsed["file_names"], graph_attr={"concentrate":"true", "imagescale": "true"}, strict=True)
        self.graph.node("START", "START", fontcolor="white", fillcolor="red", style="filled")
        self.graph.node("END", "END", fontcolor="white", fillcolor="red", style="filled")
        
        for obj in self.objects:
            object_states = [row for row in self.aggregated_table.itertuples(index=False, name=None) if obj == row[1]]
            self.transitions_list.append(np.array(object_states)[:, 2:])
            self.graph.edge("START", object_states[0][3], object_states[0][2])
            for state in range(len(object_states)):
                try:
                    self.graph.edge(object_states[state][3], object_states[state+1][3], object_states[state+1][2])
                except:
                    pass
                    self.graph.edge(object_states[state][3], "END")
                    
        for transition in self.transitions_list:
            self.state_transition = pd.DataFrame([[transition]], columns=["transitions"])
            self.transitions_dataframe = pd.concat([self.transitions_dataframe, self.state_transition]).astype(str)
        
        #Make path statistics
        self.trans_stat = pd.DataFrame(np.c_[np.unique(self.transitions_dataframe, return_counts=1)], columns=["Transition", "Count"])
        self.trans_stat.index.name = "TransitionID"  
        self.save_results()
        print(f"\nStates-transitions analysys has been succesfully performed. Actifacts saved upon: {self.output_directory}")
        
        
        
        