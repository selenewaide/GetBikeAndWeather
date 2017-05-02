#!/usr/bin/env python3

"""
Get bike and weather json files using API
"""


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
        
        if (srcdata.status_code != 200):
            print("Error - did not receive status code 200 from Open Weather!")
        
        else:
            
            # Now concatenate the time stamp with .JSON extention to create a valid filename
            filename = filestamp + "_weather.JSON"
            
            # Now write this file to disk
            filehandle = open(filename, 'w')
            filehandle.write(srcdata.text)       
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
            filehandle.write(srcdata.text)      
            filehandle.close()
        return
    
    
    def timer(self):
        counter = 0
        
        while (counter <= 1344):         
            filestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            gW = dataPull()  
            gW.getWeather(filestamp)            
            gW.getBike(filestamp)
            print("sleeping for 15 mins_", filestamp)
            time.sleep(900)           
            counter += 1    
            
if __name__ == '__main__':
    main()