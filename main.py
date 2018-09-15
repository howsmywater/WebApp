from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from math import sin, cos, sqrt, atan2, radians
import requests, json, csv
from geopy.distance import geodesic

app = Flask(__name__)
app.config['SECRET_KEY'] = "219nv8438vncjkxjfg9904jkcod4niv90"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

@app.route('/')
@app.route('/check')
def check():
    print("went into and is running")
    return render_template('about.html', title = "title")

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/api/<string:lat>/<string:long>', methods = ["GET"])
def get_stations(lat, long):
    data = {}
    data['stations'] = []
    data['stations'].append( { "STATION_NUMBER" : "01S04E32C001M",
    "LATITUDE" : "37.8073",
    "LONGITUDE" : "-121.562",
    "STATION_NAME" : "test station 1" } )

    data['stations'].append( { "STATION_NUMBER" : "00000000000",
    "LATITUDE" : "39.8073",
    "LONGITUDE" : "-131.562",
    "STATION_NAME" : "test station 2" } )

    #Above this line was just making a test JSON file to pull list of stations from
    stationlist = {}
    stationlist['stations'] = []

    point1 = (float(lat), float(long))

    for station in data['stations']:
        point2 = (float(station['LATITUDE']), float(station['LONGITUDE']))
        print(point1)
        distance = geodesic(point1, point2)
        if distance.km <= 5:
             stationlist['stations'].append(station)

    return jsonify(stationlist)

if __name__ == '__main__':
    app.run(debug=True)
