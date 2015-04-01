#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
#
# Just hosts the final data set so that app.py 
# can load it and route it as json to an endpoint
#
################################################################################



################################################################################
# Imports
################################################################################
import data
import vincent
from vincent import AxisProperties, PropertySet, ValueRef
from flask import Flask, render_template
app = Flask(__name__)

################################################################################
# Glabals
################################################################################

WIDTH = 600
HEIGHT = 300


################################################################################
# Routes
################################################################################


@app.route("/")
def index():
    return render_template('index.html')



@app.route("/data/age")
def data_age():

    bar = vincent.Bar(data.df_states['age'], width=WIDTH, height=HEIGHT)

    bar.axis_titles(x = '', y = 'Economic Score')
    ax = AxisProperties(
    	labels = PropertySet(angle = ValueRef(value = 90),
    	                     align = ValueRef(value ='left')))
    bar.axes[0].properties = ax

    return bar.to_json()


@app.route("/data/laubs")
def data_laubs():

    bar = vincent.Bar(data.df_states['laubs'], width=WIDTH, height=HEIGHT)

    bar.axis_titles(x = '', y = 'Economic Score')
    ax = AxisProperties(
    	labels = PropertySet(angle = ValueRef(value = 90),
    	                     align = ValueRef(value ='left')))
    bar.axes[0].properties = ax

    return bar.to_json()

################################################################################
# Main Execution
################################################################################

if __name__ == "__main__":
    app.run(debug=True)