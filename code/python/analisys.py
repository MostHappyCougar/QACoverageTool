import graphviz
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

class StateTransitionDiagram:
    '''
    Class to generate state transition diagram based on csv table.
    
    sequencer - is column a table will be sorted based on. Based on this column will be created a sequence of states and transitions
    order_by - Different states and transitions will be considered as related to object based on this field. If values from column order_by is same 
    for different states then these states will be related to this object
    states - the states related to object
    transitions - transitions between states
    '''
    
    def __init__(self, table_to_analizys:"DataFrame", sequencer:str, group_by:str, transitions:str, states:str, output_files:str):
        #Output files names
        self.__files = output_files
        
        #Initiate an empty dataframe
        self.__table = pd.DataFrame(columns=["seq", "object", "transitions", "states"])
        
        #Filling dataframe step by step considering multiconditional state (i.e considering values from different columns as ONE state if it is required)
        self.__table["seq"] = table_to_analizys[sequencer].astype(str).apply(", ".join, axis=1)
        self.__table["object"] = table_to_analizys[group_by].astype(str).apply(", ".join, axis=1)
        self.__table["transitions"] = table_to_analizys[transitions].astype(str).apply(", ".join, axis=1)
        self.__table["states"] = table_to_analizys[states].astype(str).apply(", ".join, axis=1)
        
        #List of transitions tat take place. Will be used for making detail statistics of states and transitions 
        self.__transitions_list = []
        self.__transitions_dataframe = pd.DataFrame(columns=["transitions"])
        self.__transitions_stats = pd.DataFrame(columns=["TransitionID", "Transition", "Count"])
        
        #List of unique objects
        self.__objects = self.__table["object"].unique()
        #List of unique states
        self.__states = self.__table["states"].unique()
        #List of unique transitions
        self.__transitions = self.__table["transitions"].unique() 
        return
        
        
    def draw_state_transitions_diagram(self) -> None:
        
        graph = graphviz.Digraph(self.__files, graph_attr={"concentrate":"true", "imagescale": "true"}, strict=True)
        #START node. All diagrams will be begin here
        graph.node("START", "START", fontcolor="white", fillcolor="red", style="filled")
        #END node. All diagrams will be end here
        graph.node("END", "END", fontcolor="white", fillcolor="red", style="filled")
        
        #Make personal list of states for each object.
        for obj in self.__objects:
            object_states = [row for row in self.__table.itertuples(index=False, name=None) if obj == row[1]]
            
            self.__transitions_list.append(np.array(object_states)[:, 2:])
            #START node links to first enter to the diagram
            graph.edge("START", object_states[0][3], object_states[0][2])
            
            #Link current state to the next one 
            for state in range(len(object_states)):
                #When last state has been reached then connect diagram to the END state
                try:
                    graph.edge(object_states[state][3], object_states[state+1][3], object_states[state+1][2])
                except:
                    pass
                    graph.edge(object_states[state][3], "END")  
        
        graph.view()
        return
    
    
    def fetch_transactions_statistics(self) -> None:
        
        for transition in self.__transitions_list:
            #Get state transition one by one
            self.__state_transition = pd.DataFrame([[transition]], columns=["transitions"])
            #Recursive add got transition to dataframe to further analisys
            self.__transitions_dataframe = pd.concat([self.__transitions_dataframe, self.__state_transition]).astype(str)
        
        #Filter only unique transactions and add them to pivot table with transitionID and counts of transition appearance
        self.__transitions_stats = pd.DataFrame(np.c_[np.unique(self.__transitions_dataframe, return_counts=1)], columns=["Transition", "Count"])
        self.__transitions_stats.index.name = "TransitionID"
        
        #Save transitions statistics
        with pd.ExcelWriter(f"{self.__files}_stats.xlsx") as writer:
            self.__transitions_stats.to_excel(writer, "TransitionsStatistics")
        
        #Save transitions statistics visualisation
        fig, (ax1) = plt.subplots()
        ax1.set(title="Transition frequency by TransitionID")
        ax1.pie(x=self.__transitions_stats["Count"], labels=self.__transitions_stats.index, autopct='%1.1f%%')
        plt.savefig(f"{self.__files}_stats_vis.pdf")
        return
        
        
        
        

        
    