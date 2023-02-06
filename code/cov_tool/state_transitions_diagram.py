import os

import graphviz as gv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import yaml

from analysis import Analysis
from save_data import ISaveData
from config_reader import IReadConfig
from input_processor import DataFrameMaker


class StateTransitionsDiagram(Analysis, ISaveData, IReadConfig):
    '''
    Realisation of Analysis abstraction for State-Transition Diagrams mod
    '''
    
    def __init__(self, config: os.PathLike):
        self.config = os.path.join(os.path.dirname(__file__), "configurations", config + ".yaml")
        self.config_parsed = {}
        self.config_parameters = {}
        

    def get_parameter(self) -> tuple:
        '''
        Get parameters related to the State-Transitions Diagrams mod
        '''
        with open(self.config) as stream:
            self.config_parsed = yaml.load(stream, yaml.FullLoader) 
            self.config_parameters["SaveTo"] = os.path.join(os.path.dirname(__file__), "output", self.config_parsed["state-transition"]["output_directory"])
            self.config_parameters["FilesName"] = self.config_parsed["state-transition"]["file_names"]
            self.config_parameters["InputDirectory"] = os.path.join(os.path.dirname(__file__), self.config_parsed["state-transition"]["input_directory"])
            self.config_parameters["Table"] = self.config_parsed["state-transition"]["input_table"]
            self.config_parameters["Sheet"] = self.config_parsed["state-transition"]["input_sheet"]
            self.config_parameters["Seq"] = self.config_parsed["state-transition"]["sequences"]
            self.config_parameters["Group"] = self.config_parsed["state-transition"]["objects"]
            self.config_parameters["Transitions"] = self.config_parsed["state-transition"]["transitions"]
            self.config_parameters["States"] = self.config_parsed["state-transition"]["states"]
            return self.config_parameters
        
        
    def save_results(self) -> None:
        '''
        Save analysis results
        '''
        self.graph.render(directory=f"{self.get_parameter()['SaveTo']}", view=False)
        
        with pd.ExcelWriter(f"{os.path.join(self.get_parameter()['SaveTo'], self.get_parameter()['FilesName'])}_stats.xlsx") as writer:
            self.trans_stat.to_excel(writer, "TransitionsStatistics")

        fig, (ax1) = plt.subplots()
        ax1.set(title="Transition frequency by TransitionID")
        ax1.pie(x=self.trans_stat["Count"], labels=self.trans_stat.index, autopct='%1.1f%%')
        plt.savefig(f"{os.path.join(self.get_parameter()['SaveTo'], self.get_parameter()['FilesName'])}_stats_vis.pdf")

    
    def analyse(self) -> None:
        '''
        Realisation of analysis method of Analysis abstract class for State-Transitions Diagram mod
        '''
        self.input_reader = DataFrameMaker(os.path.join(self.get_parameter()["InputDirectory"], self.get_parameter()["Table"]))
        self.dataframe = self.input_reader.create_dataframe(self.get_parameter()["Sheet"])
        
        self.sorted_dataframe = self.dataframe.sort_values([*self.get_parameter()["Group"], *self.get_parameter()["Seq"]])
        self.aggregated_table = pd.DataFrame(columns=["seq", "object", "transitions", "states"])
        
        self.aggregated_table["seq"] = self.sorted_dataframe[self.get_parameter()["Seq"]].astype(str).apply(", ".join, axis=1)
        self.aggregated_table["object"] = self.sorted_dataframe[self.get_parameter()["Group"]].astype(str).apply(", ".join, axis=1)
        self.aggregated_table["transitions"] = self.sorted_dataframe[self.get_parameter()["Transitions"]].astype(str).apply(", ".join, axis=1)
        self.aggregated_table["states"] = self.sorted_dataframe[self.get_parameter()["States"]].astype(str).apply(", ".join, axis=1)
        
        self.transitions_list = []
        self.transitions_dataframe = pd.DataFrame(columns=["transitions"])
        self.stransitions_stats = pd.DataFrame(columns=["TransitionID", "Transition", "Count"])
        
        self.objects = self.aggregated_table["object"].unique()
        self.states = self.aggregated_table["states"].unique()
        self.transitions = self.aggregated_table["transitions"].unique()
        
        self.graph = gv.Digraph(name=self.get_parameter()["FilesName"], graph_attr={"concentrate":"true", "imagescale": "true"}, strict=True)
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
        
        self.trans_stat = pd.DataFrame(np.c_[np.unique(self.transitions_dataframe, return_counts=1)], columns=["Transition", "Count"])
        self.trans_stat.index.name = "TransitionID"  
        self.save_results()
        print(f"\nStates-transitions analysys has been succesfully performed. Actifacts saved upon: {self.get_parameter()['SaveTo']}")
        
        
        
        