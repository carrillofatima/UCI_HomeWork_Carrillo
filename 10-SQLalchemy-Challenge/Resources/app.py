#S tep 2 - Climate App
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify
#############################################################################
# Database Setup
#############################################################################
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)
#############################################################################
# Flask Setup
#############################################################################
app = Flask(__name__)
#############################################################################
# Flask Routes
#############################################################################
# Home page

@app.route("/")
def Home_Page():
    #List all routes that are available
    """List all available api routes."""
    return (
        f"Precipitaion: /api/v1.0/precipitation<br/>"
        f"List of Stations: /api/v1.0/stations<br/>"
        f"Temperatures: /api/v1.0/tobs<br/>"
        f"Temperatures from start date: /api/v1.0/YYYY-MM-DD/<br/>"
        f"Temperatures from end date: /api/v1.0/YYYY-MM-DD/YYYY-MM-DD/<br/>")

#############################################################################
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    #Create session
    session = Session(engine)
    
    """Return date and precipitation info"""
    #Query Date and prcp
    prcp_list = session.query(Measurement.date, Measurement.prcp).all()

    #Convert the query results to a dictionary using date as the key and prcp as the value.
    prcp_range = []
    for date, prcp in prcp_list:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp

        prcp_range.append(prcp_dict)
    prcp_list = list(np.ravel(prcp_list))
    
    return jsonify(prcp_range)

  
########################################################################################
#/api/v1.0/stations
@app.route("/api/v1.0/stations")
def All_Stations():

    
    """Return list of Stations"""
    #Query Stations
    station_result = session.query(Station.station, Station.name).all()
    
    
    station_name = []
    for station, name in station_result:
        station_dict = {}
        station_dict[station] = station
        station_dict[name] = name
        station_name.append(station_dict)

 # Return a JSON list of stations from the dataset.
    return jsonify(station_name)

# ##########################################################################################
# Query the dates and temperature observations of the most active station for the last year of data.
@app.route("/api/v1.0/tobs")
def Mostactive():
    engine = create_engine("sqlite:///hawaii.sqlite")
    Base = automap_base()
    Base.prepare(engine, reflect=True)
    Base.classes.keys()

    Measurement = Base.classes.measurement
    Station = Base.classes.station

    session = Session(engine)
    """Return list of Stations"""
    #Query Stations
   
    temp_result = session.query(Measurement.tobs).\
        filter(Measurement.date >= '2016-08-23').\
        filter(Measurement.station=='USC00519281').all()
    
    # temp_station = []
    # for date, tobs in temp_result:
    #     temp_dict = {}
    #     # temp_dict[date] = date
    #     temp_dict[tobs] = tobs
    #     temp_station.append(temp_dict)
    temps = list(np.ravel(temp_result))

    return jsonify(temps=temps)

 
# Return a JSON list of temperature observations (TOBS) for the previous year.

##########################################################################################
# /api/v1.0/<start> and /api/v1.0/<start>/<end>
@app.route("/api/v1.0/<start_date>/")
def Start_date(start_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of min, avg and max tobs for a start date"""
    # Query all tobs

    start_results = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start_date).all()



    # Create a dictionary from the row data and append to a list of start_date_tobs
    start_date_tobs = []
    for data in start_results:
        start_dict = {}
        start_dict ["Start Date"] = start_date
        start_dict["MinTobs"] = data[1]
        start_dict["avgTobs"] = data[2]
        start_dict["MaxTobs"] = data[3]
        start_date_tobs.append(start_dict) 

    # start_date = list(np.ravel(start_results))
    return jsonify(start_date_tobs=start_date_tobs)

############################################################################################
@app.route("/api/v1.0/<start_date>/<end_date>/")
def Start_end_date(start_date, end_date):
    # Create our session (link) from Python to the DB
    # session = Session(engine)

    """Return a list of min, avg and max tobs for start and end dates"""
    # Query all tobs

    end_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

   
  
    # Create a dictionary from the row data and append to a list of start_end_date_tobs
    start_end_results = []
    for data_result in end_results:
        end_tobs_dict = {}
        end_tobs_dict['Start Date'] = start_date
        end_tobs_dict['End Date'] = end_date
        end_tobs_dict["MinTobs"] = float(data_result[0])
        end_tobs_dict["AvgTobs"] = float(data_result[1])
        end_tobs_dict["MaxTobs"] = float(data_result[2])

        start_end_results.append(end_tobs_dict) 
    
    # start_end_date = list(np.ravel(end_results))
    return jsonify(start_end_results)

 
if __name__ == "__main__":
    app.run(debug=True)
