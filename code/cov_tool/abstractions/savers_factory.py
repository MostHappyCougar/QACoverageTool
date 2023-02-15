from abc import ABC, abstractmethod


class ASaversFactory(ABC):
    
    @abstractmethod
    def create_state_transitions_saver(self, data: tuple):
        pass