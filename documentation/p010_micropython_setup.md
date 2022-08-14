# Setup for Micropython on the Pico

Microcontrollers a miniature computers for use with electronics.  We will be programming the [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) with the [Micropython](https://micropython.org/) language, which is an implementation of [Python 3](https://www.python.org/) for microcontrollers.  This is a powerful language in its own right, but skills developed in Python will be applicable to programming in [Java](https://en.wikipedia.org/wiki/Java_(programming_language)), [C](https://en.wikipedia.org/wiki/C_(programming_language)), or other languages.

![Raspberry Pi Pico](./img/rpi_pico_small.jpg)

You will need a Pico, a micro USB cable, and a laptop. Install the [Thonny](https://thonny.org/) program on your laptop.  Thonny will be used to write programs and to load them onto your Pico.

To set up your Pico, you'll need to get the UFC file containing the latest version of MicroPython.  Connect the micro USB cable to you Pico. Hold down the BOOTSEL button on the Pico before connecting the cable to your laptop.  A new drive should appear on the laptop.  Drag the UFC file onto the new drive.  After the file has loaded, unplug the cable from your laptop and then replug it.

Start up the Thonny application.  On the lower-right corner of the Thonny is a menu specifying which Python interpretter is running.  Click on this menu and select MicroPython.  After this, any code run in the Shell window will be executed on the Pico, rather than within your laptop.

In the main window, type the following:

```python
from machine import Pin
from utime import sleep
led = Pin('LED', Pin.OUT)
while True:
    led.on()
    sleep(0.5)
    led.off()
    sleep(2.0)
```

Save this program onto your Raspberry Pi Pico with the file name `main.py`, and then click the little green "Run" icon.  A small LED on the Pico should start blinking.  You can start and stop the program.  Modify the program to blink at different rates.

---

## Other Things to Try:
*

## References:
* MicroPython on the Pico:  https://www.raspberrypi.com/documentation/microcontrollers/micropython.html
* Latest MicroPyton UFC for the [Pico](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf): https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2
* Latest MicroPyton UFC for the [Pico W](https://datasheets.raspberrypi.com/picow/pico-w-datasheet.pdf): https://micropython.org/download/rp2-pico-w/rp2-pico-w-latest.uf2
* UFC to reset everything: https://cdn-learn.adafruit.com/assets/assets/000/099/419/original/flash_nuke.uf2
