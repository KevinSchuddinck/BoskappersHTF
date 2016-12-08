import time
import grovepi

sound_sensor = 0

grovepi.pinMode(sound_sensor, "INPUT")

while True:
	try:
		sensor_value = grovepi.analogRead(sound_sensor)
		print(sensor_value)
		time.sleep(2)
	except IOError:
		print('Error')