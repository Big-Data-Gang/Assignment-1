#!/usr/bin/env python3

import json
import math
import sys
import requests

# try:
#     latitude = float(sys.argv[1])
#     longitude = float(sys.argv[2])
#     d = float(sys.argv[3])
# except:
#     print("Argument errors. Please provide all three values")
#     sys.exit(0)

def apiCall(latitude, longitude):
    url = "http://20.185.44.219:5000/"
    data = {
        "latitude": latitude,
        "longitude": longitude
    }
    resp = requests.post(url=url, json=data)
    # print(resp.status_code)
    json_resp = resp.json()
    print(f"{json_resp['state']}-{json_resp['city']}*1")

# apiCall(latitude, longitude)
latitude = 0
longitude = 0
d = 0

def checkD(myDict:dict, lat, long, d):
    Start_Lat = myDict["Start_Lat"]
    Start_Lng = myDict["Start_Lng"]
    root = math.pow(lat-Start_Lat, 2) + math.pow(long-Start_Lng, 2)
    dist = math.sqrt(root)
    if(dist <= d):
        return True
    return False

if __name__ == "__main__":
    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        d = float(sys.argv[3])
    except:
        print("Argument errors. Please provide all three values")
        sys.exit(0)
    for line in sys.stdin:
        myDict = json.loads(line)
        if(checkD(myDict, latitude, longitude, d)):
            apiCall(myDict["Start_Lat"], myDict["Start_Lng"])

