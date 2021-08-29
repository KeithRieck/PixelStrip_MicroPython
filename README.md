# PixelStrip_MicroPython

PixelStrip is a [MicroPython](https://micropython.org/) module for controlling 
WS2812 RGB LEDs on the 
[Raspberry Pi Pico](https://www.raspberrypi.org/products/raspberry-pi-pico/). 
These LEDs are also known as 
[NeoPixels](https://learn.adafruit.com/adafruit-neopixel-uberguide).
The PixelStrip library allows you to add Animations to the strip.  Multiple strips can have separate animations that run in parallel.

Note that the included `npxl.py` module is a rough clone of AdaFruit's [Neopixel library](https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel) for [CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython). 

## TODO
* Get I2C to work on the Rpi Pico as an I2C slave, so an external master device can control the animations.
* Get pixel_order to work with RGBW pixel strips.
