"""
    Get the stock data from Yahoo finance data
    Data from the period 01 January 2017 - 24 January 2021
"""
import pandas as pd

from ydata_synthetic.preprocessing.timeseries.utils import real_data_loading

def transformations(path, seq_len: int, col='Open'):
    stock_df = pd.DataFrame(pd.read_csv(path)[col])
    try:
        stock_df = stock_df.set_index('Date').sort_index()
    except:
        stock_df=stock_df
    #Data transformations to be applied prior to be used with the synthesizer model
    data, processed_data, scaler = real_data_loading(stock_df.values, seq_len=seq_len)

    return data, processed_data, scaler