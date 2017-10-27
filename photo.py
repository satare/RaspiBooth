import Image
import pygame,sys
import time
import random
import picamera
import RPi.GPIO as GPIO  # new
from subprocess import call  

GPIO.setmode(GPIO.BCM)  # new
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)  # new


nomFichier1="/home/pi/Photos/01.jpg"
nomFichier2="/home/pi/Photos/02.jpg"
nomFichier3="/home/pi/Photos/03.jpg"
nomFichier4="/home/pi/Photos/04.jpg"
width=1280
height=960
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
		GPIO.wait_for_edge(17, GPIO.FALLING)  # new
		camera.start_preview()
		timestr = time.strftime("%Y%m%d-%H%M%S")
		nomFichier="/home/pi/Photos/"+timestr+".jpg"
		time.sleep(3)	
		camera.capture(nomFichier1,format='jpeg', resize=(photoW, photoH))
		time.sleep(1)
		camera.capture(nomFichier2,format='jpeg', resize=(photoW, photoH))
		time.sleep(1)
		camera.capture(nomFichier3,format='jpeg', resize=(photoW, photoH))
		time.sleep(1)
		camera.capture(nomFichier4,format='jpeg', resize=(photoW, photoH))
		camera.stop_preview()
		blank_image = Image.new("RGB", (width, height))
		image64 = Image.open(nomFichier1)
		image128 = Image.open(nomFichier2)
		image512 = Image.open(nomFichier3)
		image1024 = Image.open(nomFichier4)
		blank_image.paste(image64, (0+5,0+5))
		blank_image.paste(image128, ((width/2)+5,0+5))
		blank_image.paste(image512, (0+5,(height/2)+5))
		blank_image.paste(image1024, ((width/2)+5,(height/2)+5))
		blank_image.save(nomFichier)
		
		#pygame.mouse.set_visible(False)
		#screen = pygame.display.set_mode((1024,868))
		image=pygame.image.load(nomFichier)
		screen.blit(image, (0 , 0))
		
		pygame.display.update()
		time.sleep(5)

		
		#photofile = "/home/pi/Dropbox-Uploader/dropbox_uploader.sh upload "+nomFichier+" "+timestr+".jpg"  
		#call ([photofile], shell=True) 	
		#pygame.quit()
		#camera.start_preview()
		