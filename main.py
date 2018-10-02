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

all_stations = dict()

# Setup redis
with open('waterSourcesLarge.json', 'r') as f:
    for station in json.loads(f.read()):
        station_no = station['SYSTEM_NO']

        all_stations[station_no] = station

        lat = station['latitude']
        lng = station['longitude']
        red.geoadd(f'hmw:station', lng, lat, str(station_no))

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
        recentReportDf = pd.read_json("recentReport.json", orient='records')
        recentReport = pd.read_json("recentReportFindingsPSTrue.json", orient='records')
        sysList = pd.read_json("example.json", orient='records')
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
        for sysNum in numList:
            recentData = recentReport[recentReport['PRIM_STA_C'] == sysNum]
            dict = {}
            for idx, row in recentData.iterrows():
                if (report[sysNum] == "No violations!"):
                    report[sysNum] = []
                    dict['chemical'] = str(row['CHEMICAL__'])
                    dict['finding'] = str(row['FINDING'])
                    dict['mcl'] = str(row['MCL'])
                    report[sysNum].append(dict)
                else:
                    report[sysNum] += str("\nChemical: "+str(row['CHEMICAL__'])+", Finding: " +str(row['FINDING'] )+", MCL: "+ str(row['MCL']))
        return jsonify(report)

@app.route('/api/checkLocal/<int:STATION_NO>', methods = ['POST'])
def checkLocal(STATION_NO):
    activeViol = pd.read_json("activeViolations.json", orient='records')
    activeViol['WATER_SYSTEM_NUMBER'] = activeViol['WATER_SYSTEM_NUMBER'].str[2:]
    activeViol['WATER_SYSTEM_NUMBER'] = activeViol['WATER_SYSTEM_NUMBER'].apply(pd.to_numeric)
    recentReport = pd.read_json("recentReportFindingsPSTrue.json", orient='records')
    numList = [STATION_NO]
    sysNumViols = activeViol.loc[activeViol['WATER_SYSTEM_NUMBER'].isin(numList)]
    report = dict((el,"No violations!") for el in numList)

    for idx, row in sysNumViols.iterrows():
        date = str(row['ENF_ACTION_ISSUE_DATE'])
        if (report[row['WATER_SYSTEM_NUMBER']] == "No violations!"):
            report[row['WATER_SYSTEM_NUMBER']] = str("Violation Number: "+str(row['VIOLATION_NUMBER'])+", Violation Type: "+str(row['VIOLATION_TYPE_NAME'])+", Chemical: "+str(row['ANALYTE_NAME'])+", Result: "+str(row['RESULT'])+", MCL: "+str(row['MCL'])+", Action issued: "+str(row['ENF_ACTION_TYPE_ISSUED'])+", Action Issue Date: " + date)
        else:
            report[row['WATER_SYSTEM_NUMBER']] += str("\nViolation Number: "+str(row['VIOLATION_NUMBER'])+", Violation Type: "+str(row['VIOLATION_TYPE_NAME'])+", Chemical: "+str(row['ANALYTE_NAME'])+", Result: "+str(row['RESULT'])+", MCL: "+str(row['MCL'])+", Action issued: "+str(row['ENF_ACTION_TYPE_ISSUED'])+", Action Issue Date: "+date)
    for sysNum in numList:
        recentData = recentReport[recentReport['PRIM_STA_C'] == sysNum]
        for idx, row in recentData.iterrows():
            if (report[sysNum] == "No violations!"):
                report[sysNum] = str("Chemical: "+str(row['CHEMICAL__'])+", Finding: " +str(row['FINDING'] )+", MCL: "+ str(row['MCL']))
            else:
                report[sysNum] += str("\nChemical: "+str(row['CHEMICAL__'])+", Finding: " +str(row['FINDING'] )+", MCL: "+ str(row['MCL']))
    return jsonify(report)

@app.route('/api/<string:lat>/<string:lng>/<string:rad>', methods = ["GET"])
def get_stations(lat, lng, rad):
    stations = red.georadius('hmw:station', float(lng), float(lat), float(rad), 'km')
    return jsonify([all_stations[station_id] for station_id in stations][:1000])


if __name__ == '__main__':
    app.run(debug=True)
