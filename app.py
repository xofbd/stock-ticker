# author: Don Fox
# date: June 10, 2017
# file name: app.py
#
# The purpose of this script is, given a stock ticker symbol, call the stock
# ticker function and create a Bokeh plot running on Flask.

from flask import Flask, redirect, render_template, request
from stock_ticker import create_plot

app = Flask(__name__)
app.vars = {}


@app.route('/')
def main():
    return redirect('/index')


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/plot', methods=['POST'])
def plot():
    app.vars['ticker'] = request.form['ticker'].upper()

    script, div = create_plot(app.vars['ticker'])
    return render_template('plot.html', symbol=app.vars['ticker'],
                           script=script, div=div)

if __name__ == '__main__':
    app.run(port=33507, debug=False)
