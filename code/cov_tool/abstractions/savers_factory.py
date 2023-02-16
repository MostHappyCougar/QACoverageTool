from abc import ABC, abstractmethod

from abstractions.save_data import ISaveData


class ASaversFactory(ABC):
    
    @staticmethod
    @abstractmethod
    def create_state_transitions_saver(data: tuple, saver: ISaveData) -> ISaveData:
        pass