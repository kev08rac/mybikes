# Kevin Anderson

import argparse
import collections
import csv
import json
import glob
import math
from math import cos, sin, asin, sqrt
import os
import pandas as pd
import re
import requests
import string
import sys
import time
import xml


def distance(lon1, lat1, lon2, lat2):
    lon1 = float(lon1)
    lon2 = float(lon2)
    lat1 = float(lat1)
    lat2 = float(lat2)
    x = (lon2 - lon1) * cos(0.5 * (lat2 + lat1))
    y = (lat2 - lat1)
    return R * sqrt(x * x + y * y)


baseURL = sys.argv[1]

station_statusURL = baseURL + '/station_status.json'
station_infoURL = baseURL + '/station_information.json'

requestsDataStatus = requests.get(station_statusURL)
dataJSONStatus = requestsDataStatus.json()
dfStatus = pd.DataFrame(dataJSONStatus['data']['stations'])

requestsDataInfo = requests.get(station_infoURL)
dataJSONInfo = requestsDataInfo.json()
dfInfo = pd.DataFrame(dataJSONInfo['data']['stations'])

if sys.argv[2] == 'total_bikes':
    sum_bikes = dfStatus['num_bikes_available'].sum()
    print("Command=" + sys.argv[2])
    print("Parameters=")
    print("Output=" + str(sum_bikes))

if sys.argv[2] == 'total_docks':
    sum_docks = dfStatus['num_docks_available'].sum()
    print("Command=" + sys.argv[2])
    print("Parameters=")
    print("Output=" + str(sum_docks))

if sys.argv[2] == 'percent_avail':
    station_id_num = sys.argv[3]
    str(station_id_num)
    index = dfStatus.query('station_id == @station_id_num')['num_docks_available']
    index = index.to_string(index=False)
    index = int(index, 10)
    sum_bikes_available = dfStatus.query('station_id == @station_id_num')['num_bikes_available']
    sum_bikes_available = sum_bikes_available.to_string(index=False)
    sum_bikes_available = int(sum_bikes_available, 10)
    percentageRaw = float(index / (sum_bikes_available + index))
    percentage = math.trunc((percentageRaw * 100))
    print("Command=" + "percent_avail")
    print("Parameters=" + station_id_num)
    print("Output=" + str(percentage) + "%")

if sys.argv[2] == 'closest_stations':
    lat = sys.argv[3]
    lon = sys.argv[4]
    R = 6371000

    stationList = sorted(dfInfo.to_dict('records'), key=lambda d: distance(d["lon"], d["lat"], lon, lat))

    print("Command= closest_stations")
    print("Parameters= " + str(lat) + " " + str(lon))
    print("Output=")
    for x in stationList[:3]:
        print(x['station_id'] + ", " + x['name'])

if sys.argv[2] == 'closest_bike':
    lat = sys.argv[3]
    lon = sys.argv[4]
    R = 6371000

    stationList = sorted(dfInfo.to_dict('records'), key=lambda d: distance(d["lon"], d["lat"], lon, lat))
    nearestStationID = []

    for i in range(0, 10):
        nearestStationID.append(stationList[i]['station_id'])
        hasBike = dfStatus.query('station_id == @nearestStationID')['num_bikes_available']
        hasBike = hasBike.to_string(index=False)
        if hasBike != "0":
            correctStationID = stationList[i]['station_id']
            correctStationName = stationList[i]['name']
            break

    print("Command=closest_bike")
    print("Parameters=" + str(lat) + " " + str(lon))
    print("Output=" + str(correctStationID) + ", " + str(correctStationName))