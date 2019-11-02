import time
import board
from drivers import Pin

LED = Pin(board.PIN_LED, Pin.OUTPUT)

while True:
    LED.toggle()
    time.sleep(0.5)
