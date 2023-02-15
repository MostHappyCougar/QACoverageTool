from abstractions import savers_factory
from savers import state_transitions_saver

class SaversFactory(savers_factory.ASaversFactory):
    
    @staticmethod
    def create_state_transitions_saver(data: tuple):
        return state_transitions_saver.StateTransitionsDiagramsSaver(data)