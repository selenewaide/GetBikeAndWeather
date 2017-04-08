#!/usr/bin/env python3
'''
Created on 15 Mar 2017
@author: David Fottrell
'''
import time
import datetime
import requests

def main():
    dP = dataPull()
    dP.timer()
    return

class dataPull(object):
    '''
    classdocs
    
    This class was created to facilitate pulling in API data at regular intervals.  At this point, it is configured
    to pull in current weather data for Dublin from www.openweathermap.org, at 5 minute intervals.
    
    The same data structure can be used to pull in data from other sources on the same time interval.
    
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    
    def getWeather(self):
        # This is a variable to contain the www.openweathermap.org call for current weather in Dublin with an API key
        srcdata = requests.get('http://api.openweathermap.org/data/2.5/weather?id=7778677&APPID=0b1d40f0f5b1bc4af97416f01400dd72&units=metric')
        
        # For later, use TRY: and EXCEPT: functions as taught in Web Dev class
        
        if (srcdata.status_code != 200):
            print("Error - did not receive status code 200 from Open Weather!")
        
        else:
            # Create a unique filename to identify the JSON data based on date and time
            # This should pull a time stamp in the format of YYYMMDD-HHMMSS
            filestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            # Now concatenate the time stamp with .JSON extention to create a valid filename
            filestamp = filestamp + "_weather.JSON"
            
            # Now write this file to disk
            filehandle = open(filestamp, 'w')
            filehandle.write(srcdata.text)       # TypeError: write() argument must be str, not Response
            filehandle.close()
        return
    
    def getBike(self):
        srcdata = requests.get('https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=40d8ce05c637ce862bae2802f93241044b3a73d8')
        
        if (srcdata.status_code != 200):
            print("Error - did not receive status code 200 from Dublin Bikes!")
        
        else:
            # Create a unique filename to identify the JSON data based on date and time
            # This should pull a time stamp in the format of YYYMMDD-HHMMSS
            filestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            # Now concatenate the time stamp with .JSON extention to create a valid filename
            filestamp = filestamp + "_bikes.JSON"
            
            # Now write this file to disk
            filehandle = open(filestamp, 'w')
            filehandle.write(srcdata.text)       # TypeError: write() argument must be str, not Response
            filehandle.close()
        return
    
    
    def timer(self):
        counter = 0
        # Note - requests should not be more than once every 10 minutes
        # This timer will be used to prevent excessive calls to the bikes API
        while (counter <= 12):          # This is for testing phase only, will change to a large number when proven
            gW = dataPull()  
            gW.getWeather()            # Calls the pullBikes class to execute a current bikes pull
            gW.getBike()
            time.sleep(900)           # Timing function waits 15 mins after triggering the data pull
            counter += 1    
            
if __name__ == '__main__':
    main()