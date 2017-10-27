#import Image
import pygame,sys
import time
import random
import picamera
import os
from PIL import Image
import RPi.GPIO as GPIO  # new
from subprocess import call

#VARS
#GPIO Pin Nbr to trigger the photo process
gpio_pin=17
#final size of your canva
width=1024
height=768



dir_path = os.path.dirname(os.path.realpath(__file__))

#end Vars


#Check if there is any usb drive plugged
#while not os.path.isdir("/media/pi"):
#  time.sleep(5)
#  print "Please connect Usb Key"

#usbPaths=os.listdir("/media/pi")
#while not len(usbPaths):
#   print "Please connect Usb Key"
#   usbPaths=os.listdir("/media/pi")
#   time.sleep(5)

#Ok, USB Drive available
#usbPath=usbPaths[0]
#photo_path=usbPath+"Photos/"
photo_path="/home/pi/Photos/"#for debug
if not os.path.isdir(photo_path):
  os.mkdir(photo_path)

GPIO.setmode(GPIO.BCM)  # new
GPIO.setup(gpio_pin, GPIO.IN, GPIO.PUD_UP)  # new

photoW=(width/2)-10
photoH=(height/2)-10

with picamera.PiCamera() as camera:

	#camera.hflip = True
	pygame.init()
	dispInfo =  pygame.display.Info()
	myfont = pygame.font.SysFont("monospace", 62)
	screen = pygame.display.set_mode((dispInfo.current_w, dispInfo.current_h))
	pygame.mouse.set_visible(False)
	while True:
		image=pygame.image.load(dir_path+"/welcome.jpeg")
		screen.blit(image, (0 , 0))
		pygame.display.update()
		#GPIO.wait_for_edge(gpio_pin, GPIO.FALLING)  # new
                time.sleep(6)
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
		#for x in range(1, 4):
		#	os.remove(photo_path+x+".jpg")
		time.sleep(5)
		sys.exit()
