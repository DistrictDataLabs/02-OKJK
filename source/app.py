#!/usr/bin/env python
# -*- coding: utf-8 -*-

import data
import vincent
from vincent import AxisProperties, PropertySet, ValueRef
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

### Vincent Data Routes
WIDTH = 600
HEIGHT = 300

@app.route("/data/age")
def data_age():

    bar = vincent.Bar(data.df_states['age'], width=WIDTH, height=HEIGHT)

    bar.axis_titles(x = '', y = 'Age')
    ax = AxisProperties(
    	labels = PropertySet(angle = ValueRef(value = 90),
    	                     align = ValueRef(value ='left')))
    bar.axes[0].properties = ax

    return bar.to_json()


@app.route("/data/laubs")
def data_laubs():

    bar = vincent.Bar(data.df_states['laubs'], width=WIDTH, height=HEIGHT)

    bar.axis_titles(x = '', y = 'Unemployment')
    ax = AxisProperties(
    	labels = PropertySet(angle = ValueRef(value = 90),
    	                     align = ValueRef(value ='left')))
    bar.axes[0].properties = ax

    return bar.to_json()


@app.route("/data/staging")
def data_staging():
    
    return """{
  "width": 400,
  "height": 200,
  "padding": {"top": 10, "left": 30, "bottom": 20, "right": 10},
  "data": [
    {
      "name": "table",
      "values": [
        {"x":"A", "y":28}, {"x":"B", "y":55}, {"x":"C", "y":43},
        {"x":"D", "y":91}, {"x":"E", "y":81}, {"x":"F", "y":53},
        {"x":"G", "y":19}, {"x":"H", "y":87}, {"x":"I", "y":52}
      ]
    }
  ],
  "scales": [
    {"name":"x", "type":"ordinal", "range":"width", "domain":{"data":"table", "field":"data.x"}},
    {"name":"y", "range":"height", "nice":true, "domain":{"data":"table", "field":"data.y"}}
  ],
  "axes": [
    {"type":"x", "scale":"x"},
    {"type":"y", "scale":"y"}
  ],
  "marks": [
    {
      "type": "rect",
      "from": {"data":"table"},
      "properties": {
        "enter": {
          "x": {"scale":"x", "field":"data.x"},
          "width": {"scale":"x", "band":true, "offset":-1},
          "y": {"scale":"y", "field":"data.y"},
          "y2": {"scale":"y", "value":0}
        },
        "update": { "fill": {"value":"steelblue"} },
        "hover": { "fill": {"value":"red"} }
      }
    }
  ]
}"""

# @app.route("/data/line")
# def data_line():
#     return vincent.Line(data.list_data, width=WIDTH, height=HEIGHT).to_json()


# @app.route("/data/multiline")
# def data_multiline():
#     return vincent.Line(data.multi_iter1, width=WIDTH, height=HEIGHT, iter_idx=('index')).to_json()


# @app.route("/data/stocks")
# def stocks():
#     line = vincent.Line(data.price[['MSFT', 'AAPL']], width=WIDTH, height=HEIGHT)
#     line.axis_titles(x='Date', y='Price')
#     line.legend(title='MSFT vs AAPL')
#     return line.to_json()


# @app.route("/data/scatter")
# def scatter():
#     scatter = vincent.Scatter(data.multi_iter2, width=WIDTH, height=HEIGHT, iter_idx='index')
#     scatter.axis_titles(x='Index', y='Data Value')
#     scatter.legend(title='Categories')
#     return scatter.to_json()


# @app.route("/data/stacked_stocks")
# def stacked_stocks():
#     stacked = vincent.StackedArea(data.price, width=WIDTH, height=HEIGHT)
#     stacked.axis_titles(x='Date', y='Price')
#     stacked.legend(title='Tech Stocks')
#     stacked.colors(brew='Accent')
#     return stacked.to_json()


# @app.route("/data/stacked_bar")
# def stacked_bar():
#     stack = vincent.StackedBar(data.df_states, width=WIDTH, height=HEIGHT)
#     stack.axis_titles(x='state_name', y='age')
#     stack.legend(title='Unemployment by State')
#     stack.scales['x'].padding = 0.2
#     stack.colors(brew='Pastel1')
#     return stack.to_json()


if __name__ == "__main__":
    app.run(debug=True)