# cloudy-a

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Build Status](https://travis-ci.com/stubs/cloudy-a.svg?branch=feature%2Frefactor_cloudy-a)](https://travis-ci.com/stubs/cloudy-a)

A refactor of [DJAckbar's Cloudy-a](https://github.com/DJAkbar/cloudy-a) script for LED light animations according to the weather forecast. 
For an example see [Youtube](https://www.youtube.com/watch?v=DNXssI4LuMc).


#### Setup:
+ Ensure that pigpio is up and running
`sudo pigpiod` will start the service
+ [Consider Cron for scheduling on the Raspberry Pi](https://www.raspberrypi.org/documentation/linux/usage/cron.md)

#### Helpful links:
+ [Setting up the RPI and LED Strip](https://dordnung.de/raspberrypi-ledstrip/)
+ [Dark Sky API](https://darksky.net/dev/login?next=/account)
+ [GPIOZero Documentation](https://gpiozero.readthedocs.io/en/stable/)
+ [Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/)