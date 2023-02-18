from abc import ABC, abstractmethod

import pandas as pd


class IFormatTable(ABC):
    
    @staticmethod
    @abstractmethod
    def highlite_zero(table: pd.DataFrame) -> pd.DataFrame:
        pass