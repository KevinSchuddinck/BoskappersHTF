import time
import grovepi
import json
import requests

button = 3
grovepi.pinMode(button, "INPUT")

buzzer = 8
grovepi.pinMode(buzzer, "OUTPUT")

url = 'http://192.168.50.148:4000/api'
headers = {"team", "sensor"}

while True:
    try:
        if grovepi.digitalRead(button):
			data = {
						team: { id: [3] }
						sensor: {
							id: [0]
							state: [true]
							value: [1]
							}
					})
			r = requests.post(url, headers, stats = json.dumps(data))
			print(r.text)
			grovepi.digitalWrite(buzzer,1)
			time.sleep(1)
			grovepi.digitalWrite(buzzer,0)
		
    except IOError:
        print ("Error")