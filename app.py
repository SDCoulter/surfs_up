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