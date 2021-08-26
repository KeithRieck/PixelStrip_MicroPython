import array
import time
from machine import Pin
import rp2

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def __pio_for_ws2812():
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
    def __init__(self, pin_num, num_pixels, bpp=3, brightness=1.0, auto_write=True, pixel_order=None):
        self.pin = Pin(pin_num)
        self._pin_num = pin_num
        self._num_pixels = num_pixels
        self._bpp = bpp
        self._brightness = brightness
        self.auto_write = auto_write
        self._pixel_order = pixel_order
        self._ar = array.array("I", [0 for _ in range(num_pixels)])
        self._sm = rp2.StateMachine(0, __pio_for_ws2812, freq=8_000_000, sideset_base=self.pin)
        self._sm.active(1)
    
    def deinit(self):
        self.fill((0, 0, 0, 0))
        self.show()
        # self.pin.deinit()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.deinit()

    def __repr__(self):
        return "[" + ", ".join([str(x) for x in self]) + "]"

    def _set_item(self, index, r, g, b, w): 
        self._ar[index] = (g<<16) + (r<<8) + b

    def __setitem__(self, index, color):
        self._set_item(index, color[0], color[1], color[2], color[3])
        if self.auto_write:
            self.show()

    def __getitem__(self, index):
        c = self._ar[index]
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
        for index in range(self._num_pixels):
            self._set_item(index, color[0], color[1], color[2], color[3])
        if self.auto_write:
            self.show()

    @property
    def n(self):
        return len(self)

    @property
    def bpp(self):
        return self._bpp

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        self._brightness = min(max(value, 0.0), 1.0)
        if self.auto_write:
            self.show()

# TODO:
# how to use libraries and multiple files on RPi?
# Add and test PixelStrip module
#
# I2C as a peripheral device
# Test with two strips
