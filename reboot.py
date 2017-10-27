import time
#import picamera
import RPi.GPIO as GPIO  # new



def halt():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output
	
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # new
GPIO.setup(23, GPIO.IN, GPIO.PUD_UP)  # new
GPIO.wait_for_edge(23, GPIO.FALLING)  # new
#halt()
