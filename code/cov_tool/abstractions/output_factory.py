from abc import ABC, abstractmethod

from abstractions.save_output import ISaveOutput


class AOutputFactory(ABC):
    
    @staticmethod
    @abstractmethod
    def make_state_trans_output(data: tuple, saver: ISaveOutput) -> ISaveOutput:
        pass