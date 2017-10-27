RaspiBooth
==========
*Photobooth application for raspberry*
Use
 - Python
 - pygame
 - picamera

How to install
--------------------------

 - With git:

	sudo apt-get install git
	go to your install directory (can be Home)
	cd
	git clone https://github.com/satare/RaspiBooth.git

 - Or via direct download :

	download Zipfile from Github, un-zip to your app directory (can be "home")

and you're done!

How to launch at startup ?
--------------------------
On your Pi, edit the file */etc/rc.local* (you must be Root).

    sudo nano /etc/rc.local

add :

    /yourPathToRaspiBooth/raspi_booth.sh &

Gpio pins description :
-----------------------

![Raspberry Pi Gpio Description](https://github.com/satare/RaspiBooth/blob/master/doc/raspberry-pi-gpio-layout-revision-1.png?raw=true)
