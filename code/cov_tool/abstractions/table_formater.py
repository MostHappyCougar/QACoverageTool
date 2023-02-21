from abc import ABC, abstractmethod

import pandas as pd


class IFormatTable(ABC):
    
    @staticmethod
    @abstractmethod
    def highlite_zero(table: pd.DataFrame) -> pd.DataFrame.style:
        pass
    
    
    @staticmethod
    @abstractmethod
    def make_borders(table: pd.DataFrame.style) -> pd.DataFrame.style:
        pass
    
    
    @staticmethod
    @abstractmethod
    def format_columns(table: pd.DataFrame.style) -> pd.DataFrame.style:
        pass
    
    
    @staticmethod
    @abstractmethod
    def format_index(table: pd.DataFrame.style) -> pd.DataFrame.style:
        pass