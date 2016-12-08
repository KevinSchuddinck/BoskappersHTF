import time
import grovepi

sound_sensor = 0

grovepi.pinMode(sound_sensor, "INPUT")

while True:
	try:
		temp = grovepi.analogRead(sound_sensor)
		sensor_value = (20 * log10(temp + 1) )
		print(sensor_value)
		time.sleep(2)
	except IOError:
		print('Error')