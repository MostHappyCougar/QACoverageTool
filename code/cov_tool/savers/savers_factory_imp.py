from abstractions import savers_factory
from savers.state_transitions_saver import StateTransitionsDiagramsSaver

class SaversFactory(savers_factory.ASaversFactory):
    
    @staticmethod
    def create_state_transitions_saver(data: tuple, saver=StateTransitionsDiagramsSaver) -> StateTransitionsDiagramsSaver:
        return saver(data)