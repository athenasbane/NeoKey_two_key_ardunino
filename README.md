# NeoKey_two_key_ardunino

## Description

I wanted a project to have two keys that mute/unmute microphone and turn on and off camera on Zoom with a LED to show if it's both are on or not. I spotted this project:  

![image](https://user-images.githubusercontent.com/62559903/147848414-2ec18f04-e60a-4774-9d57-a9b1d42d63b9.png)

I thought it suited my needs and would help me learn about microcontrollers so nievely bought the the parts needed. However, I couldn't find a guide for this project anywhere. This was frustrating at first given my very limited knowledge of microcontrollers, CircuitPython (python in general), arduninos etc. I was lost and didn't know where to start. In restrospect however, this has been a great learning experience. 

I'll use this project to document my findings so should anyone else have the same issues I faced you have some of the information needed all in one place. 

## What you need to know before you get started:

### Me 

I'm a frontend software engineer with little to no knowledge of python, know that you use any code or guidance at your own risk. Given my software experience I am very good at searching for information and debugging. Use this project as a resource not a step by step guide, this is meant to be a learning experience for you also, have fun and experiment for yourself you will likely find things that can be improved. If you do PLEASE TELL ME!

### Skills

This project requires solidering experience, at least, I can't find the parts used that come pre-solidered. 

## What you need:

- Breadboard
- Jumper cables 
- NeoKey Socket Breakout x 2 - https://www.adafruit.com/product/4978
- Cherry Mx Keyboard Switch of your choice x 2 - I used Cherry Mx Blues but I which I had used Cherry Mx Black. You can use anything with a Kailh socket
- QtPy - There's lots of varients I used this one - https://www.adafruit.com/product/4600

## Setup 

Solider the pins on to your QtPy and two NeoKey Sockets push your switches into the sockets

![image](https://user-images.githubusercontent.com/62559903/147848414-2ec18f04-e60a-4774-9d57-a9b1d42d63b9.png)

Starting on the top:

### Wiring

** QT PY **
#### Top
- GND Pin -> GND Rail
- 3v Pin -> POWER Rail
#### Bottom
- A1 Pin -> NeoKey 2 - A Pin
- A2 Pin -> NeoKey 1 - A Pin
- A3 Pin -> NeoKey 1 - I Pin

** NeoKey 1 ** 
Make sure the orientation of the NeoKey is the correct: + - 0 A C on top
- Positive Pin -> POWER Rail
- Minus Pin -> GND Rail
- O Pin -> NeoKey 2 - I Pin
- C Pin -> GND Rail

** NeoKey 2 ** 
- Positive Pin -> POWER Rail
- Minus Pin -> GND Rail
- C Pin -> GND Rail

## Software Setup

Now you have set all that up plug it into your computer. I followed this guide [Welcome to CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython?view=all) to setup Micropython. 

## Copying Libraries 

I had an issue with dragging and dropping libraries in to the due to the limited storage space on the QT PY so I had to use `cp -X` or `cp -RX` in terminal on mac as the GUI Copy and Paste / move copies something called Extended Attributes (I don't know what they are either). 

## Libraries 

You add nessessary libraries/dependancies by adding them to lib directory

