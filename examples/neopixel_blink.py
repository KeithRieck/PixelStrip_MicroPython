import time
from npxl import NeoPixel

strip = NeoPixel(22, 8)
strip.fill((0, 0, 0, 0))

while True:
    strip[1] = (0, 128, 0, 0)
    strip.show()
    time.sleep(1.0)
    strip.fill((0, 0, 0, 0))
    strip.show()
    time.sleep(1.0)
    
