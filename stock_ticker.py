# author: Don Fox
# date: June 9, 2017
# file name: stock_ticker.py
#
# The purpose of this script is to plot the closing price for the month of May
# 2017.

import pandas as pd
import requests

from bokeh.plotting import figure
from bokeh.embed import components


def create_plot(ticker_symbol):

    # URL for stock symbol
    URL_prefix = 'https://www.quandl.com/api/v3/datasets/WIKI/'
    URL_suffix = '.json?trim_start=2017-05-01&trim_end=2017-05-31'
    URL = URL_prefix + ticker_symbol + URL_suffix

    # get json and create pandas DataFrame
    r = requests.get(URL)
    json_data = r.json()['dataset']
    stock_data = pd.DataFrame(
        data=json_data['data'], columns=json_data['column_names'])
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])

    # create bokeh plot
    p = figure(x_axis_type="datetime", title="May 2017 Stock Closing Price")
    p.grid.grid_line_alpha = 0.3
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Price ($)'

    p.line(stock_data.Date,
           stock_data.Close, color='blue', legend=ticker_symbol)
    p.legend.location = 'top_left'

    script, div = components(p)
    return script, div
