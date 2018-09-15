from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from math import sin, cos, sqrt, atan2, radians
import pandas as pd
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

@app.route('/test')
def test():
    url = url_for('checkLocal')

@app.route('/home/<int:STATION_NO>', methods = ["POST"])
def get_analysis(STATION_NO):
    url = "this"

@app.route('/api/check', methods = ['POST'])
def checkArea():
    if request.method == "POST":
        activeViol = pd.read_json("activeViolations.json", orient='records')
        activeViol['WATER_SYSTEM_NUMBER'] = activeViol['WATER_SYSTEM_NUMBER'].str[2:]
        activeViol['WATER_SYSTEM_NUMBER'] = activeViol['WATER_SYSTEM_NUMBER'].apply(pd.to_numeric)

    sysList = pd.read_json(request.get_json(), orient = 'records')
    sysList['SYSTEM_NO'] = sysList['SYSTEM_NO'].apply(pd.to_numeric)
    numList = sysList.SYSTEM_NO.unique()
    sysNumViols = activeViol.loc[activeViol['WATER_SYSTEM_NUMBER'].isin(numList)]

        report = dict((el,"No violations!") for el in numList)

        for idx, row in sysNumViols.iterrows():
            date = str(row['ENF_ACTION_ISSUE_DATE'])
            if (report[row['WATER_SYSTEM_NUMBER']] == "No violations!"):
                report[row['WATER_SYSTEM_NUMBER']] = str("Violation Number: "+str(row['VIOLATION_NUMBER'])+", Violation Type: "+str(row['VIOLATION_TYPE_NAME'])+", Chemical: "+str(row['ANALYTE_NAME'])+", Result: "+str(row['RESULT'])+", MCL: "+str(row['MCL'])+", Action issued: "+str(row['ENF_ACTION_TYPE_ISSUED'])+", Action Issue Date: " + date)
            else:
                report[row['WATER_SYSTEM_NUMBER']] += str("\nViolation Number: "+str(row['VIOLATION_NUMBER'])+", Violation Type: "+str(row['VIOLATION_TYPE_NAME'])+", Chemical: "+str(row['ANALYTE_NAME'])+", Result: "+str(row['RESULT'])+", MCL: "+str(row['MCL'])+", Action issued: "+str(row['ENF_ACTION_TYPE_ISSUED'])+", Action Issue Date: "+date)

        return jsonify(report)

@app.route('/api/checkLocal/<int:STATION_NO>', methods = ['POST'])
def checkLocal(STATION_NO):
    
    return jsonify(report)

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
        distance = geodesic(point1, point2)
        if distance.km <= 5:
             stationlist['stations'].append(station)

    with open('example.json', 'w') as outfile:
        json.dump(list, outfile)

    return jsonify(stationlist)


if __name__ == '__main__':
    app.run(debug=True)
