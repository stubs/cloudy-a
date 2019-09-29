#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import sys
import time

from colorzero import Color
from darksky.api import DarkSky
from gpiozero import RGBLED

DARK_SKY_API = "YOUR_API_KEY"  # https://darksky.net/dev/register
LAT = 0.0
LONG = 0.0


# These are the different animations for the LED-strips:
def rain(led):
    led.off()  # ensure starting from off
    for i in range(20):
        led.pulse(
            random.uniform(0.2, 0.6),
            random.uniform(0.2, 0.6),
            on_color=Color("blue"),
            n=1,
        )
        time.sleep(random.uniform(0.1, 1))


def cloud(led):
    led.off()
    for i in range(20):
        led.pulse(
            random.uniform(0.2, 0.3),
            random.uniform(0.2, 0.3),
            on_color=Color("white"),
            n=1,
        )
        time.sleep(random.uniform(0.5, 1))


def sun(led):
    led.off()
    for i in range(20):
        led.pulse(
            random.uniform(0.05, 0.06),
            random.uniform(0.05, 0.06),
            on_color=Color("yellow"),
            n=1,
        )
        time.sleep(random.uniform(0.1, 0.5))


def snow(led):
    led.off()
    for i in range(15):
        led.pulse(
            random.uniform(0.5, 2),
            random.uniform(0.5, 2),
            on_color=Color("darkslategrey"),
            n=1,
        )
        time.sleep(random.uniform(0.5, 1))


def flash(led):
    led.off()
    for i in range(10):
        led.pulse(
            random.uniform(0.05, 0.06),
            random.uniform(0.05, 0.06),
            on_color=Color("darkslategrey"),
            n=1,
        )
        time.sleep(random.uniform(0.5, 1))
        led.pulse(
            random.uniform(0.05, 0.06),
            random.uniform(0.05, 0.06),
            on_color=Color("darkgoldenrod"),
            n=1,
        )
        time.sleep(random.uniform(0.5, 1))
        led.pulse(
            random.uniform(0.05, 0.06),
            random.uniform(0.05, 0.06),
            on_color=Color("blue"),
            n=1,
        )
        time.sleep(random.uniform(0.5, 1))


def unknown_icon(led):
    led.off()
    for i in range(10):
        led.pulse(
            random.uniform(0.05, 0.06),
            random.uniform(0.05, 0.06),
            on_color=Color("purple"),
            n=1,
        )
        time.sleep(1)


weather_dict = {
    "clear-day": sun,
    "clear-night": sun,
    "cloudy": cloud,
    "fog": cloud,
    "partly-cloudy-day": cloud,
    "partly-cloudy-night": cloud,
    "rain": rain,
    "sleet": snow,
    "snow": snow,
    "unknown_icon": unknown_icon,
    "wind": sun,
}


def main_loop():
    pi_led = RGBLED(17, 22, 24)
    darksky = DarkSky(DARK_SKY_API)
    forecast = darksky.get_forecast(LAT, LONG).currently.icon
    if weather_dict.get(forecast):
        weather_dict[forecast](pi_led)
    else:
        weather_dict["unknown_icon"]()


if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\nExiting by user request.\n")
        sys.exit(0)
