#!/bin/sh

python shut_and_reboot.py 23 & # arg : gpio pin to trigger reboot

photoDir="/home/pi/Photos/"
if [ ! -d "$photoDir" ]; then
  mkdir $photoDir -R
  # Control will enter here if $DIRECTORY doesn't exist.
fi

sudo mount /dev/sda1 $photoDir -o uid=pi,gid=pi
python photo.py $photoDir 17 & # arg1 : photoDir, arg2 : gpioPin to trigger
