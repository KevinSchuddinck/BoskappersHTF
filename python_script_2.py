import time
import grovepi
import math

sound_sensor = 0
grovepi.pinMode(sound_sensor, "INPUT")

buzzer = 8
grovepi.pinMode(buzzer, "OUTPUT")

threshold_value = 55

while True:
	try:
		temp = grovepi.analogRead(sound_sensor)
		sensor_value = (20 * math.log10(temp + 1) )
		print(sensor_value)
		if sensor_value > threshold_value :
			print('ALARM!')
			grovepi.digitalWrite(buzzer,1)
			time.sleep(1)
			grovepi.digitalWrite(buzzer,0)
		else:
			time.sleep(.5)
			
	except IOError:
		print('Error')