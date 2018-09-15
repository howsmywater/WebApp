from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from math import sin, cos, sqrt, atan2, radians
import requests, json, csv, redis
from geopy.distance import geodesic

app = Flask(__name__)
app.config['SECRET_KEY'] = "219nv8438vncjkxjfg9904jkcod4niv90"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
redis_port = 6379
redis_host = "localhost"
redis_password = ""

red = redis.StrictRedis(redis_host, redis_port, redis_password)

@app.route('/')
@app.route('/check')
def check():
    print("went into and is running")
    return render_template('about.html', title = "title")


@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/api/ ')

@app.route('/api/<string:lat>/<string:long>', methods = ["GET"])
def get_stations(lat, long):
    data = {}
    data['stations'] = []
    data['stations'].append( { "SYSTEM_NO" : "01S04E32C001M",
    "LATITUDE" : "37.8073",
    "LONGITUDE" : "-121.562",
    "SYSTEM_NAM" : "test station 1" } )

    data['stations'].append( { "SYSTEM_NO" : "00000000000",
    "LATITUDE" : "39.8073",
    "LONGITUDE" : "-131.562",
    "SYSTEM_NAM" : "test station 2" } )

    #Above this line was just making a test JSON file to pull list of stations from
    stationlist = {}
    stationlist['stations'] = []

    point1 = (float(lat), float(long))

    testPoint = (37.672371, -121.839577)

    with open('waterSourcesSmall.json', 'r') as f:
        list = json.loads(f.read())

    for station in list:
        point2 = (float(station['latitude']), float(station['longitude']))
        print(point1)
        distance = geodesic(testPoint, point2)
        if distance.km <= 5:
             stationlist['stations'].append(station)

    with open('example.json', 'w') as outfile:
        json.dump(data, outfile)

    return jsonify(stationlist)


if __name__ == '__main__':
    app.run(debug=True)
