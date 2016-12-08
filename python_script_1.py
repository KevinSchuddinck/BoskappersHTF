import time
import grovepi

button = 3
grovepi.pinMode(button, "INPUT")

buzzer = 8
grovepi.pinMode(buzzer, "OUTPUT")

while True:
    try:
        if grovepi.digitalRead(button):
			grovepi.digitalWrite(buzzer,1)
			time.sleep(1)
			grovepi.digitalWrite(buzzer,0)
		
    except IOError:
        print ("Error")