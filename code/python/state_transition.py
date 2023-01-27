import graphviz
import pandas as pd

class StateTransitionDiagram:
    '''
    Class to generate state transition diagram based on csv table
    sequencer - is column a table will be sorted based on. Based on this column will be created a sequence of states and transitions
    object_id_is - Different states and transitions will be considered as related to object based on this field. If values from column object_id_is is same 
    for different states then these states will be related to this object
    states - the states related to object
    transitions - transitions between states
    '''
    
    def __init__(self, table_to_analizys:"DataFrame", sequencer:str, object_id_is:str, transitions:str, states:str):
        self.__obj_name = object_id_is
        
        #Initiate an empty dataframe
        self.__table = pd.DataFrame(columns=["seq", "object", "transitions", "states"])
        
        #Filling dataframe step by step considering multiconditional state (i.e considering values from different columns as ONE state if it is required)
        self.__table["seq"] = table_to_analizys[sequencer].astype(str).apply(", ".join, axis=1)
        self.__table["object"] = table_to_analizys[object_id_is].astype(str).apply(", ".join, axis=1)
        self.__table["transitions"] = table_to_analizys[transitions].astype(str).apply(", ".join, axis=1)
        self.__table["states"] = table_to_analizys[states].astype(str).apply(", ".join, axis=1)
        
        #List of unique objects
        self.__objects = self.__table["object"].unique()
        #List of unique states
        self.__states = self.__table["states"].unique()
        #List of unique transitions
        self.__transitions = self.__table["transitions"].unique() 
        return
        
        
    def draw_state_transitions_diagram(self) -> None:
        
        graph = graphviz.Digraph(comment="name_of_graph", graph_attr={"concentrate":"false"})
        graph.node("START", "START", fontcolor="white", fillcolor="red", style="filled")
        graph.node("END", "END", fontcolor="white", fillcolor="red", style="filled")
        
        for obj in self.__objects:
            object_states = [i for i in self.__table.itertuples(index=False) if obj == i[1]]
            graph.edge("START", object_states[0][3])
            for rng in range(len(object_states)):
                try:
                    graph.edge(object_states[rng][3], object_states[rng+1][3], object_states[rng+1][2])
                except:
                    graph.edge(object_states[rng][3], "END")
        graph.view()
        return
        
        
        

        
    