import time
import board
import neopixel
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull

# board neopixel
pixel1 = neopixel.NeoPixel(board.NEOPIXEL, 1)

# two neo key neopixels
pixel2 = neopixel.NeoPixel(board.A3, 2)

switch1 = DigitalInOut(board.A1)
switch1.direction = Direction.INPUT
switch1.pull = Pull.UP
switch1_status = False
switch1_awaiting_change = False

switch2 = DigitalInOut(board.A2)
switch2.direction = Direction.INPUT
switch2.pull = Pull.UP
switch2_status = True
switch2_awaiting_change = False

pixel1.fill((0, 255, 0))

kbd = Keyboard(usb_hid.devices)

while True:
    if not switch1.value and not switch1_awaiting_change:
        switch1_awaiting_change = True
    elif switch1.value and switch1_awaiting_change:
        switch1_status = not switch1_status
        switch1_awaiting_change = False
        kbd.press(Keycode.CONTROL, Keycode.COMMAND, Keycode.SHIFT, Keycode.A)
        time.sleep(.09)
        kbd.release(Keycode.CONTROL, Keycode.COMMAND, Keycode.SHIFT, Keycode.A)

    if not switch2.value and not switch2_awaiting_change:
        switch2_awaiting_change = True
    elif switch2.value and switch2_awaiting_change:
        switch2_status = not switch2_status
        switch2_awaiting_change = False
        kbd.press(Keycode.CONTROL, Keycode.COMMAND, Keycode.SHIFT, Keycode.S)
        time.sleep(.09)
        kbd.release(Keycode.CONTROL, Keycode.COMMAND, Keycode.SHIFT, Keycode.S)
    

    if not switch1.value and switch1_awaiting_change:
        pixel2[1] = (255, 255, 0)
    elif switch1_status:
        pixel2[1] = (255, 0, 0)
    else:
        pixel2[1] = (0, 255, 0)

    if not switch2.value and switch2_awaiting_change:
        pixel2[0] = (255, 255, 0)
    elif switch2_status:
        pixel2[0] = (255, 0, 0)
    else:
        pixel2[0] = (0, 255, 0)

    pixel2.show()
    time.sleep(0.01)
