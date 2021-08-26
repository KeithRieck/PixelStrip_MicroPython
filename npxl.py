import array
import time
from machine import Pin
import rp2

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()


class NeoPixel:
    def __init__(self, pin_num, num_pixels, brightness=0.5):
        self._pin_num = pin_num
        self._num_pixels = num_pixels
        self._brightness = brightness
        self._ar = array.array("I", [0 for _ in range(num_pixels)])
        self._sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(pin_num))
        self._sm.active(1)
    
    def __setitem__(self, index, color):
        self._ar[index] = (color[1]<<16) + (color[0]<<8) + color[2]

    def __getitem__(self, c):
        return (((c >> 8) & 0xFF), ((c>>16) & 0xFF), (c & 0xFF), 0)
    
    def __len__(self):
        return self._num_pixels
    
    def show(self):
        dimmer_ar = array.array("I", [0 for _ in range(self._num_pixels)])
        for i,c in enumerate(self._ar):
            r = int(((c >> 8) & 0xFF) * self._brightness)
            g = int(((c >> 16) & 0xFF) * self._brightness)
            b = int((c & 0xFF) * self._brightness)
            dimmer_ar[i] = (g<<16) + (r<<8) + b
        self._sm.put(dimmer_ar, 8)
        time.sleep_ms(10)
    
    def fill(self, color):
        for p in range(self._num_pixels):
            self[p] = color


# TODO:
# rename ws2812 to __pio_for_ws2812
# auto_write in constructor
# brightness in constructor
# NOOP constructor arguments for bpp and pixel_order
# __repr__
# deinit and __enter__ and __exit__
# n as a property for strip length
#
# how to use libraries and multiple files on RPi?
# Add and testPixelStrip stuff
#
# I2C as a peripheral device
# Test with two strips