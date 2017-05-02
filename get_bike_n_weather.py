#!/usr/bin/env python3

import time
import datetime
import requests

def main():
    dP = dataPull()
    dP.timer()
    return

class dataPull(object):

    def __init__(self):
        '''
        Constructor
        '''
    
    
    def getWeather(self, filestamp):
        # This is a variable to contain the www.openweathermap.org call for current weather in Dublin with an API key
        srcdata = requests.get('http://api.openweathermap.org/data/2.5/weather?id=7778677&APPID=0b1d40f0f5b1bc4af97416f01400dd72&units=metric')
        
        # For later, use TRY: and EXCEPT: functions as taught in Web Dev class
        
        if (srcdata.status_code != 200):
            print("Error - did not receive status code 200 from Open Weather!")
        
        else:
            
            # Now concatenate the time stamp with .JSON extention to create a valid filename
            filename = filestamp + "_weather.JSON"
            
            # Now write this file to disk
            filehandle = open(filename, 'w')
            filehandle.write(srcdata.text)       # TypeError: write() argument must be str, not Response
            filehandle.close()
        return
    
    def getBike(self, filestamp):
        srcdata = requests.get('https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=40d8ce05c637ce862bae2802f93241044b3a73d8')
        
        if (srcdata.status_code != 200):
            print("Error - did not receive status code 200 from Dublin Bikes!")
        
        else:
            
            # Now concatenate the time stamp with .JSON extention to create a valid filename
            filename = filestamp + "_bikes.JSON"
            
            # Now write this file to disk
            filehandle = open(filename, 'w')
            filehandle.write(srcdata.text)       # TypeError: write() argument must be str, not Response
            filehandle.close()
        return
    
    
    def timer(self):
        counter = 0
        # Note - requests should not be more than once every 10 minutes
        # This timer will be used to prevent excessive calls to the bikes API
        while (counter <= 1344):          # This is for testing phase only, will change to a large number when proven
            filestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            gW = dataPull()  
            gW.getWeather(filestamp)            # Calls the pullBikes class to execute a current bikes pull
            gW.getBike(filestamp)
            print("sleeping for 15 mins_", filestamp)
            time.sleep(900)           # Timing function waits 15 mins after triggering the data pull
            counter += 1    
            
if __name__ == '__main__':
    main()