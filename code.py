"""
Two Key mute and video keyboard using NeoKey Sockets

Libraries:
    adafruit_hid
    adafruit_pypixelbuf.mpy
    neopixel.mpy

"""
import sys
import time
import board
import neopixel
import usb_hid
import supervisor
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull

# Keyboard setup
kbd = Keyboard(usb_hid.devices)

# board neopixel
qtpy_neopixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

# The two neo key neopixels
video_mute_neopixel = neopixel.NeoPixel(board.A3, 2)

# Mute Switch Setup
mute_switch = DigitalInOut(board.A1)
mute_switch.direction = Direction.INPUT
mute_switch.pull = Pull.UP
mute_switch_status = False
mute_switch_awaiting_change = False
# Change these to what ever suits your use case 
mute_keyboard_keys = [Keycode.CONTROL, Keycode.COMMAND, Keycode.SHIFT, Keycode.S]

# Video Switch Setup
video_switch = DigitalInOut(board.A2)
video_switch.direction = Direction.INPUT
video_switch.pull = Pull.UP
video_switch_status = True
video_switch_awaiting_change = False
# Change these to what ever suits your use case 
video_keyboard_keys = [Keycode.CONTROL, Keycode.COMMAND, Keycode.SHIFT, Keycode.A]

# Global Variables
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

# Serial variables 
microphone_on = "MICROPHONE_ON"
microphone_off = "MICROPHONE_OFF"
video_on = "VIDEO_ON"
video_off = "VIDEO_OFF"


# Green When connected
qtpy_neopixel.fill(green)

# node doesn't send the EOF character so have to loop through
def non_blocking_read():
    i = ""
    while supervisor.runtime.serial_bytes_available:
        i += sys.stdin.read(1)
    return i

while True:
    if supervisor.runtime.serial_bytes_available:
        value = non_blocking_read()
        print(value)
        if value == microphone_on:
            mute_switch_status = False
        elif value == microphone_off:
            mute_switch_status = True
        elif value == video_on:
            video_switch_status = False
        elif value == video_off:
            video_switch_status = True

    if not mute_switch.value and not mute_switch_awaiting_change:
        mute_switch_awaiting_change = True
    elif mute_switch.value and mute_switch_awaiting_change:
        mute_switch_status = not mute_switch_status
        mute_switch_awaiting_change = False
        kbd.press(*mute_keyboard_keys)
        time.sleep(.09)
        kbd.release(*mute_keyboard_keys)

    if not video_switch.value and not video_switch_awaiting_change:
        video_switch_awaiting_change = True
    elif video_switch.value and video_switch_awaiting_change:
        video_switch_status = not video_switch_status
        video_switch_awaiting_change = False
        kbd.press(*video_keyboard_keys)
        time.sleep(.09)
        kbd.release(*video_keyboard_keys)

    if not video_switch.value and video_switch_awaiting_change:
        video_mute_neopixel[0] = yellow
    elif video_switch_status:
        video_mute_neopixel[0] = red
    else:
        video_mute_neopixel[0] = green

    if not mute_switch.value and mute_switch_awaiting_change:
        video_mute_neopixel[1] = yellow
    elif mute_switch_status:
        video_mute_neopixel[1] = red
    else:
        video_mute_neopixel[1] = green

    video_mute_neopixel.show()
    time.sleep(.01)
