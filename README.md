RaspiBooth
==========
*Photobooth application for raspberry*

Use :
 - Python
 - pygame
 - picamera

How to install
--------------------------

Prerequisites :

      sudo apt-get install python python-picamera python3-picamera python-rpi.gpio python-pygame python-pil 

 - With git:
	 - sudo apt-get install git
	 - go to your install directory (can be *home*)   
		 - cd
	 - git clone https://github.com/satare/RaspiBooth.git

 - Or via direct download :
	 - download Zipfile from Github
	 - un-zip to your app directory (can be
	   "home")

chmod +x raspi_booth.sh
chmod +x shut_and_reboot.sh

... And you're done!

How to launch at startup ?
--------------------------
On your Pi, edit the file */etc/rc.local* (you must be Root).

    sudo nano /etc/rc.local

add :

    /yourPathToRaspiBooth/raspi_booth.sh &

Gpio pins description :
-----------------------
When you take your pi ethernet port up :
Connect ground and gpio [1-25] to temporary switch

![Raspberry Pi Gpio Description](https://github.com/satare/RaspiBooth/blob/master/doc/raspberry-pi-gpio-layout-revision-1.png?raw=true)
