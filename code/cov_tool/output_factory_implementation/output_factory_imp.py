from abstractions.output_factory import AOutputFactory
from output_factory_implementation.state_transitions_output import StateTransitionsDiagramOutput

class OutputFactory(AOutputFactory):
    
    @staticmethod
    def make_state_trans_output(data: tuple, output_model=StateTransitionsDiagramOutput) -> StateTransitionsDiagramOutput:
        '''
        Output will be created based on chosen model. All output files will be formated according to the model also
        '''
        return output_model(data)