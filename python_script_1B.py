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

while True:
    try:
        if grovepi.digitalRead(button):
			stats = {
						'team': { 'id': [3] },
						'sensor': {
							'id': [0],
							'state': [1],
							'value': ['ALARM']
							}
					}
			r = requests.post(url, headers = headers, data = json.dumps(stats))
			print(r.text)
			grovepi.digitalWrite(buzzer,1)
			time.sleep(1)
			grovepi.digitalWrite(buzzer,0)
		
    except IOError:
        print ("Error")