import time
import grovepi
import json
import requests

button = 3
grovepi.pinMode(button, "INPUT")

buzzer = 8
grovepi.pinMode(buzzer, "OUTPUT")

url = 'http://192.168.50.148:4000/api'
headers = {"Content-type": "application/json"}

switch = 1

while True:
    try:
	if switch :
        if grovepi.digitalRead(button):
			stats = {
						'team': { 'id': [3] },
						'sensor': {
							'id': [0],
							'state': [1],
							'value': ['ALARM AAN']
							}
					}
			r = requests.post(url, headers = headers, data = json.dumps(stats))
			print(r.text)
			grovepi.digitalWrite(buzzer,1)
			switch = 0
			#time.sleep(1)
			#grovepi.digitalWrite(buzzer,0)
	else:
		if grovepi.digitalRead(button):
			stats = {
						'team': { 'id': [3] },
						'sensor': {
							'id': [0],
							'state': [0],
							'value': ['ALARM AF']
							}
					}
			r = requests.post(url, headers = headers, data = json.dumps(stats))
			print(r.text)
			grovepi.digitalWrite(buzzer,0)
			switch = 1
		
		
    except IOError:
        print ("Error")