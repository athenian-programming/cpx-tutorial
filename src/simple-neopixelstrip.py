import neopixel
import board

# On a CPX use board.A1
# On a CLUE use board.A3 for connector #1

pixels = neopixel.NeoPixel(board.A3, 30, brightness = .5)
while True:
    for i in range(30):
        pixels[i] = (0, 0, 255)
    for i in range(30):
        pixels[i] = (255, 0, 0)
