import time
import os
import serial
import VisionAlgorithm2 as vision
import os.path
import subprocess
import time
import RPi.GPIO as GPIO

class Servo:

    def __init__(self) :
        GPIO.setmode(GPIO.BOARD)
		GPIO.setup(7, GPIO.OUT)
		self.pwm = GPIO.PWM(7, 50)
		print 'Lens Servo Setup'

    def rotateServo(self, angle) :
        duty = float(angle) / 18.0 + 2.5
        pwm.start(duty)
        time.sleep(0.5)
        pwm.stop()	

class piCam :

	def __init__(self):
		self.serialCom = serial.Serial('/dev/tty.usbmodem1421', 9600)
		self.lensServo = Servo()

	def takePicture(fileName) :
		cmd = 'raspistill -o ' + fileName + ' -t 1 -n'
		pid = subprocess.call(cmd, shell=True)

	def waitForSerial(key) :
		active = True
		while active :
			val = ser.readline()
			if val == key :
				active = False

	def switchToVisible() :
		ser.write(b'B')
		waitForSerial('F')

	def switchToInfrared() :
		ser.write(b'B')
		waitForSerial('E')

	def parseImage()
		vis = 'visible' + str(iteration) + '.jpg'
		infra = 'infrared' + str(iteration) + '.jpg'

		takePicture(vis)
		switchToInfrared()
		takePicture(infra)
		switchToVisible()
			
		if os.path.isfile(vis) and os.path.isfile(infra) :
			vision.classifyImage(vis, infra)
		else :
			print 'File does not exist'

		
		