# Import dependencies.
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# Import Flask dependency.
from flask import Flask, jsonify

# Set up our SQLite engine.
engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect the database into our classes.
Base = automap_base()
# Reflect our tables.
Base.prepare(engine, reflect=True)
# Save our references to each table (as Classes).
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create a session link from Python to our database.
session = Session(engine)

# Define our app for Flask application.
# Create a new Flask instance.
app = Flask(__name__)

# Create a route - first define the root, then a function (route).
# Added <br/> tags for newline purposes.
@app.route('/')
def welcome():
    return (
    '''
    Welcome to the Climate Analysis API!<br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end<br/>
    ''')

# Create the precipitation route.
@app.route('/api/v1.0/precipitation')
def precipitation():
    # Calculate the date one year before the data ends.
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(365)
    # Run a query to get the date and precipitation for the previous year.
    precipitation = session.query(Measurement.date, Measurement.prcp)\
                    .filter(Measurement.date >= prev_year)
    # Create a dictionary with the date as the key, and precip as the value.
    # Dictionary comprehension to loop through the query and store as dict.
    precip = {date: prcp for date, prcp in precipitation}
    # Return the jsonify'd dictionary.
    return jsonify(precip)

# Create the stations route.
@app.route('/api/v1.0/stations')
def station():
    # Run a query to get the list of station names.
    results = session.query(Station.station).all()
    # Unravel the query return and store the data as a list.
    stations = list(np.ravel(results))
    # Return the data from the list as a JSON.
    return jsonify(stations=stations)

# Create the temperature observations route.
@app.route('/api/v1.0/tobs')
def temp_monthly():
    # Calculate date from one year ago.
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(365)
    # Query the primary station for all the temperature observations from 
    # the previous year.
    results = session.query(Measurement.tobs)\
                .filter(Measurement.station == 'USC00519281')\
                .filter(Measurement.date >= prev_year).all()
    # Unravel the array and store as a list, return the jsonfy.
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Create the statistics route.
@app.route('/api/v1.0/temp/<start>')
@app.route('/api/v1.0/temp/<start>/<end>')
def stats(start=None, end=None):
    # Create a list to select our statistical values.
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    # Use an if statement to find out if user entered end date.
    # Run if statement if no end date entered.
    if not end:
        # Pass an asterisk to indicate multiple statistical parts to our query.
        results = session.query(*sel).\
                    filter(Measurement.date >= start).\
                    filter(Measurement.date <= end).all()
        # Unravel and return JSON.
        temps = list(np.ravel(results))
        return jsonify(temps)

    # If there is an end date provided run the following.
    results = session.query(*sel).\
                filter(Measurement.date >= start).\
                filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)