import time
import grovepi
import math

sound_sensor = 0

grovepi.pinMode(sound_sensor, "INPUT")

while True:
	try:
		temp = grovepi.analogRead(sound_sensor)
		sensor_value = (20 * math.log10(temp + 1) )
		print(sensor_value)
		time.sleep(.5)
	except IOError:
		print('Error')