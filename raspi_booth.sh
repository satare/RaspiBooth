#!/bin/sh
#param :
photoDir="/home/pi/Photos/"
#end params


#launch python script for reboot
python shut_and_reboot.py 4 & # arg : gpio pin to trigger reboot

#create photoDir
if [ ! -d "$photoDir" ]; then
  mkdir $photoDir -R
fi

#first usbKey is /dev/sda1 (first partition)
sudo mount /dev/sda1 $photoDir -o uid=pi,gid=pi
#launch photobooth script
python photo.py $photoDir 3 & # arg1 : photoDir, arg2 : gpioPin to trigger
