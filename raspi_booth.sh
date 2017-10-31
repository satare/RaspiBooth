#!/bin/sh
#param :
photoDir="/home/pi/Photos/" #Don't forget the Slash \m/
photoGPIO=3
resetGPIO=4
#end params


#launch python script for reboot
python shut_and_reboot.py $resetGPIO & # arg : gpio pin to trigger reboot

#create photoDir and mount usbkey into
if [ ! -d "$photoDir" ]; then
  mkdir $photoDir -R
fi

#first usbKey is /dev/sda1 (first partition)
sudo mount /dev/sda1 $photoDir -o uid=pi,gid=pi
#launch photobooth script
python photo.py $photoDir $photoGPIO  # arg1 : photoDir, arg2 : gpioPin to trigger ; no "&" 
