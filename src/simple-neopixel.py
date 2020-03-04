import neopixel
import board

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness = .01)
while True:
    for i in range(10):
        pixels[i] = (0, 0, 255)
