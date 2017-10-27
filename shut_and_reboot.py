import time
import RPi.GPIO as GPIO

#vars
gpioShutdownPort=23
#when some gpio-port it triggered, reboot of halt the Pi, depending on the time button is holded down.

def halt():
    command = "/usr/bin/sudo /sbin/shutdown -h -P now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output

def reboot():
    command = "/usr/bin/sudo /sbin/shutdown -r now"
    import subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print output

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # new
GPIO.setup(gpioShutdownPort, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # new

while True:
    GPIO.wait_for_edge(gpioShutdownPort, GPIO.FALLING)
    start = time.time()
    time.sleep(0.2)

    while GPIO.input(gpioShutdownPort) == GPIO.LOW:
        time.sleep(0.01)
    length = time.time() - start

    if length > 3:
        halt()
    else:
        reboot()
