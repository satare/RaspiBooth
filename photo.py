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
#end Vars

dir_path = os.path.dirname(os.path.realpath(__file__))
photo_path="/home/pi/Photos/"#for debug

welcomePic=dir_path+"/welcome.jpeg"


#Ok, USB Drive available
#usbPath=usbPaths[0]
#photo_path=usbPath+"Photos/"
if not os.path.isdir(photo_path):
  os.mkdir(photo_path)

GPIO.setmode(GPIO.BCM)  # new
GPIO.setup(gpio_pin, GPIO.IN, GPIO.PUD_UP)  # new

def createCanva(myImages,nomFinalFichier):
    border=10
    # all images must be the same size
    imgwidth= Image.open(myImages[0])
    width, height = imgwidth.size

    canvaSize=((width*2)+(3*border), ((height*2)+(3*border)))

    blank_image = Image.new("RGB", canvaSize)
    image64 = Image.open(myImages[0])
    image128 = Image.open(myImages[1])
    image512 = Image.open(myImages[2])
    image1024 = Image.open(myImages[3])

    blank_image.paste(image64, (0+border,0+border))
    blank_image.paste(image128, ((canvaSize[0]/2)+border/2,0+border))
    blank_image.paste(image512, (0+border,(canvaSize[1]/2)+border/2))
    blank_image.paste(image1024, ((canvaSize[0]/2)+border/2,(canvaSize[1]/2)+border/2))
    blank_image.save(nomFinalFichier)


pygame.init()
dispInfo=pygame.display.Info()

def splash(fileName):
    #pygame.init()
    #dispInfo =  pygame.display.Info()
    FinalImage=Image.open(fileName) # open fullsize
    FinalImage=FinalImage.resize((dispInfo.current_w, dispInfo.current_h), Image.ANTIALIAS) # resize image
    FinalImage.save(photo_path+"/preview.jpeg")
    image=pygame.image.load(photo_path+"/preview.jpeg")
    screen.blit(image, (0 , 0))
    pygame.display.update()


#Check if there is any usb drive plugged
#while not os.path.isdir("/media/pi"):
#  time.sleep(5)
#  print "Please connect Usb Key"

#usbPaths=os.listdir("/media/pi")
#while not len(usbPaths):
#   print "Please connect Usb Key"
#   usbPaths=os.listdir("/media/pi")
#   time.sleep(5)




with picamera.PiCamera() as camera:
    pygame.init()
    camera.vflip = True
    myfont = pygame.font.SysFont("monospace", 62)
    screen = pygame.display.set_mode((dispInfo.current_w, dispInfo.current_h))
    pygame.mouse.set_visible(False)
    while True:
        allImages=[]
        splash(welcomePic)
        #GPIO.wait_for_edge(gpio_pin, GPIO.FALLING)  # new
        time.sleep(3) ## only for debugging
        camera.start_preview()
        timestr = time.strftime("%Y%m%d-%H%M%S")
        nomFinalFichier=photo_path+timestr+".jpg" #final canva filename
        time.sleep(3)
        for x in range(1, 5):
            FullSizeFileName=photo_path+str(timestr)+"_"+str(x)+".jpg" #fullsize picture filename
            camera.capture(FullSizeFileName,format='jpeg') # take a pic, name it
            allImages.append(FullSizeFileName)
            time.sleep(1)

        createCanva(allImages,nomFinalFichier)
        camera.stop_preview()
        splash(nomFinalFichier)

        time.sleep(5)
        sys.exit()
