#!/usr/bin/env python3

import json
import sys
import datetime

def checkDesc(string):
    desc = ["lane blocked" , "shoulder blocked" , "overturned vehicle"]

    for i in desc:
        if i in string:
            return True
    return False


def checkConditions(myDict:dict = None):
    if myDict == None:
        return None
    
    if float("nan") in list(myDict.values()):
        return False

    try:
        #if (any([i in myDict["Description"].lower() for i in ["lane blocked" , "shoulder blocked" , "overturned vehicle"]])) and (myDict["Severity"] >=2) and (myDict["Sunrise_Sunset"].lower() == "night") and (myDict["Visibility(mi)"] <= 10) and (myDict["Precipitation(in)"] >= 0.2) and (any([i == myDict["Weather_Condition"].lower() for i in ["heavy snow", "thunderstorm", "heavy rain", "heavy rain showers", "blowing dust"]])):
            #return True
        if checkDesc(myDict['Description'].lower()):
            if myDict['Severity'] >= 2:
                if myDict['Sunrise_Sunset'] == 'Night':
                    if myDict['Visibility(mi)'] <= 10:
                        if myDict['Precipitation(in)'] >= 0.2:
                            if myDict['Weather_Condition'].lower() in ["heavy snow", "thunderstorm", "heavy rain", "heavy rain showers", "blowing dust"]:
                                return True
    except:
        return False
    return False



for line in sys.stdin:
    myDict = json.loads(line)
    status = checkConditions(myDict)
    if status:
        time = datetime.datetime.strptime(myDict["Start_Time"], "%Y-%m-%d %H:%M:%S")
        if time.hour < 12:
            print("0" + str(time.hour), 1)
        else:
            print(time.hour, 1) 
    
   