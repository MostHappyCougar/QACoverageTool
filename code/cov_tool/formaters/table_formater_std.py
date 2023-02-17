import pandas as pd
import numpy as np

from abstractions.table_formater import IFormatTable

class StandardTableFormater(IFormatTable):
        
    @staticmethod
    def highlite_zero(table:pd.DataFrame)->pd.DataFrame:
        return table.style.applymap(StandardTableFormater.zero_highliter)
    
    
    @staticmethod
    def zero_highliter(value):
        color = 'red' if value == 0 else None
        return 'background-color: {}'.format(color)
    
    
    @staticmethod
    def make_borders(table: pd.DataFrame.style) -> pd.DataFrame.style:
        return table.set_properties(**{"border": "1px solid black"})
    
    
    @staticmethod
    def format_columns(table: pd.DataFrame.style) -> pd.DataFrame.style:
        return table.applymap_index(StandardTableFormater.columns_formater, axis="columns")
    
    
    @staticmethod
    def columns_formater(value):
        return "background-color: #FDFF6A; font-weight: bold; border: 1px solid black" if value != None else None
    
    
    @staticmethod
    def format_index(table: pd.DataFrame.style) -> pd.DataFrame.style:
        return table.applymap_index(StandardTableFormater.index_formater, axis="index")
    
    
    @staticmethod
    def index_formater(value):
        return "background-color: #6D95EC; font-weight: bold; border: 1px solid black" if value != None else None
    
    
    @staticmethod
    def highlite_margins_bot(table: pd.DataFrame.style) -> pd.DataFrame.style:
        idx = pd.IndexSlice
        slice_ = idx[idx['_ValuesOccurCount'], :]
        return table.applymap(StandardTableFormater.margins_highliter_bot, subset=slice_)
    
    
    @staticmethod
    def margins_highliter_bot(value):
        return np.where(value != None, "border: 1px solid black; background-color: #CDCDCD;", None)
    
    
    @staticmethod
    def highlite_margins_right(table: pd.DataFrame.style) -> pd.DataFrame.style:
        idx = pd.IndexSlice
        slice_ = idx[:, idx['_ValuesOccurCount']]
        return table.applymap(StandardTableFormater.margins_highliter_right, subset=slice_)
    
    
    @staticmethod
    def margins_highliter_right(value):
        return np.where(value != None, "border: 1px solid black; background-color: #CDCDCD;", None)
    
    
    

    
        