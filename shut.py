import time
#import picamera
import RPi.GPIO as GPIO  # new



def halt():
    command = "/usr/bin/sudo /sbin/shutdown -h -P now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output
	
GPIO.setmode(GPIO.BCM)  # new
GPIO.setup(22, GPIO.IN, GPIO.PUD_UP)  # new

GPIO.wait_for_edge(22, GPIO.FALLING)  # new
halt()
