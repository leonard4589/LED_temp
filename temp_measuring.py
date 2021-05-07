# if T = x, then x - 10 = the number of lights to light up.
import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 20)
T = 13
x = T - 10
for i in range(0,20,x):
  pixels[i] = (255,0,0)
