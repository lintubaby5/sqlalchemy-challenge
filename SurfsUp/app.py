import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify



#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine,reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """Welcome to Climate Analysis API. Below are the Available API routes"""
    return (
        f"Welcome to Climate Analysis API. Below are the Available API routes<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    #calculate previous year based on the last entry in the table
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    #calculate precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    session.close()
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    #retrive all the stations in the table
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    session.close()
    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def temp_monthly():
     session = Session(engine)
     prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)
     #calculate all the temperature reported at the highest reported station for the previous year
     results = session.query(Measurement.tobs).\
         filter(Measurement.station == 'USC00519281').\
         filter(Measurement.date >= prev_year).all()
     temps = list(np.ravel(results))
     session.close()
     return jsonify(temps=temps)

#app route that takes dynamic values
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
# Add parameters to `stats(): start / start and end parameters
def stats(start=None, end=None):
    session = Session(engine)
    # calculate Max, Min and Avg temperature
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    #calculate the max, min and avg temperature for the start or start and end date entered
    if not end:
        results = session.query(*sel).\
			filter(Measurement.date >= start).\
			filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)
    results = session.query(*sel).\
		filter(Measurement.date >= start).\
		filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

if __name__ == "__main__":
    app.run(debug=True)