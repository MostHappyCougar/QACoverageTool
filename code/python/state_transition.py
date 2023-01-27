import graphviz
import pandas as pd

class StateTransitionDiagram:
    '''
    Class to generate state transition diagram based on csv table.
    
    sequencer - is column a table will be sorted based on. Based on this column will be created a sequence of states and transitions
    order_by - Different states and transitions will be considered as related to object based on this field. If values from column order_by is same 
    for different states then these states will be related to this object
    states - the states related to object
    transitions - transitions between states
    '''
    
    def __init__(self, table_to_analizys:"DataFrame", sequencer:str, group_by:str, transitions:str, states:str):
        #Initiate an empty dataframe
        self.__table = pd.DataFrame(columns=["seq", "object", "transitions", "states"])
        
        #Filling dataframe step by step considering multiconditional state (i.e considering values from different columns as ONE state if it is required)
        self.__table["seq"] = table_to_analizys[sequencer].astype(str).apply(", ".join, axis=1)
        self.__table["object"] = table_to_analizys[group_by].astype(str).apply(", ".join, axis=1)
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
        
        graph = graphviz.Digraph(comment="name_of_graph", graph_attr={"concentrate":"false", "imagescale": "true"})
        #START node. All diagrams will be begin here
        graph.node("START", "START", fontcolor="white", fillcolor="red", style="filled")
        #END node. All diagrams will be end here
        graph.node("END", "END", fontcolor="white", fillcolor="red", style="filled")
        
        #Make personal list of states for each object.
        for obj in self.__objects:
            object_states = [row for row in self.__table.itertuples(index=False) if obj == row[1]]
            #START node links to first enter to the diagram
            graph.edge("START", object_states[0][3])
            
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
        
        
        

        
    