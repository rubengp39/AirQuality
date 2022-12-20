import json
import time
import requests

# api-endpoint
URL = "http://api.weatherapi.com/v1/current.json?key=3817edbde7fd4412a26182206221312&q=Bilbao&aqi=yes"


startTime = time.time()
endTime = startTime + 43200

while(time.time() < endTime):
    file = open('weatherData.json', 'a')
    r = requests.get(url=URL)
    data = r.json()
    data = json.dumps(data)
    file.write(data)
    file.write(",")
    file.close()
    time.sleep(900)
