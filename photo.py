import Image
import pygame,sys
import time
import random
import picamera
import os
import RPi.GPIO as GPIO  # new
from subprocess import call

#VARS
#GPIO Pin Nbr to trigger the photo process
gpio_pin=17
#final size of your canva
width=1280
height=960


dir_path = os.path.dirname(os.path.realpath(__file__))
photo_path=usbPath+"Photos/"
#end Vars


#Check if there is any usb drive plugged
usbPaths=os.listdir("/media/pi")
while not len(usbPaths):
    print "Please connect Usb Key"
    usbPaths=os.listdir("/media/pi")
    time.sleep(5)

#Ok, USB Drive available
usbPath=usbPaths[0]
GPIO.setmode(GPIO.BCM)  # new
GPIO.setup(gpio_pin, GPIO.IN, GPIO.PUD_UP)  # new

photoW=(width/2)-10
photoH=(height/2)-10

with picamera.PiCamera() as camera:
	camera.hflip = True
	pygame.init()
	pygame.mouse.set_visible(False)
	myfont = pygame.font.SysFont("monospace", 62)
	screen = pygame.display.set_mode((width,height))

	while True:

		image=pygame.image.load("welcome.jpeg")
		screen.blit(image, (0 , 0))
		pygame.display.update()
		GPIO.wait_for_edge(gpio_pin, GPIO.FALLING)  # new
		camera.start_preview()
		timestr = time.strftime("%Y%m%d-%H%M%S")

		nomFinalFichier=photo_path+timestr+".jpg" #final canva filename
		time.sleep(3)
		for x in range(1, 4):
			tmpResizedFileName=photo_path+x+".jpg" #resized file name, temp
			FullSizeFileName=photo_path+timestr+"_"+x+".jpg" #fullsize picture filename
			camera.capture(FullSizeFileName,format='jpeg') # take a pic, name it
			img=Image.open(FullSizeFileName)# open fullsize
			img = img.resize((photoW, photoH), Image.ANTIALIAS)# resize image
			img.save(tmpResizedFileName) # save image to temp file, ready to paste to canva
			time.sleep(1)

		camera.stop_preview()
		blank_image = Image.new("RGB", (width, height))
		image64 = Image.open(photo_path+"1.jpg")
		image128 = Image.open(photo_path+"2.jpg")
		image512 = Image.open(photo_path+"3.jpg")
		image1024 = Image.open(photo_path+"4.jpg")

		blank_image.paste(image64, (0+5,0+5))
		blank_image.paste(image128, ((width/2)+5,0+5))
		blank_image.paste(image512, (0+5,(height/2)+5))
		blank_image.paste(image1024, ((width/2)+5,(height/2)+5))
		blank_image.save(nomFinalFichier)

		image=pygame.image.load(nomFinalFichier)
		screen.blit(image, (0 , 0))
		pygame.display.update()
		for x in range(1, 4):
			os.remove(photo_path+x+".jpg")
		time.sleep(5)
