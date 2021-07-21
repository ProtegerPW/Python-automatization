#! /usr/bin/python3
# weather.py - Prints the weather for a location from the command line.
# You have to use your own Api key from openweathermap.org 
import sys, requests, json

if len(sys.argv) < 3:
    print('Usage: ./ch_14_weather.py <API key> <location>')
    sys.exit()

apiKey = sys.argv[1]
location = ' '.join(sys.argv[2:])

url ='http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location, apiKey)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)

w = weatherData
print('Current weather in %s:' % (location))
print(w['weather'][0]['main'], '-', w['weather'][0]['description'])