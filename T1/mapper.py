#!/usr/bin/env python3

import json
import sys
import datetime

def checkConditions(myDict:dict = None):
    if myDict == None:
        return None
    if (any([i in myDict["Description"] for i in ["lane blocked" , "shoulder blocked" , "overturned vehicle"]])) and (myDict["Severity"] >=2) and (myDict["Sunrise_Sunset"] == "Night") and (myDict["Visibility(mi)"] <= 10) and (myDict["Precipitation(in)"] >= 0.2) and (any([i in myDict["Weather_Condition"] for i in ["Heavy Snow", "Thunderstorm", "Heavy Rain", "Heavy Rain Showers", "Blowing Dust"]])):
        return True
    return False



for line in sys.stdin:
    myDict = json.loads(line)
    status = checkConditions(myDict)
    if status:
        time = datetime.datetime.strptime(myDict["Start_Time"], "%Y-%m-%d %H:%M:%S")
        #print(time.hour, type(time.hour))
        if time.hour < 12:
            print("0" + str(time.hour), 1)
        else:
            print(time.hour, 1) 
   