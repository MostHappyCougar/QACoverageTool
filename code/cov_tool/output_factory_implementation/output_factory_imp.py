from abstractions.output_factory import AOutputFactory
from output_factory_implementation.state_transitions_output import StateTransitionsDiagramOutput

class SaversFactory(AOutputFactory):
    
    @staticmethod
    def make_state_trans_output(data: tuple, saver=StateTransitionsDiagramOutput) -> StateTransitionsDiagramOutput:
        return saver(data)