from typing import Optional

from fastapi import FastAPI

import RPi.GPIO as GPIO

import board
import busio
import digitalio
from adafruit_mcp230xx.mcp23017 import MCP23017

inpin = 4
outpin = 17
npins = 10

i2c = busio.I2C(board.SCL, board.SDA)
mcp = MCP23017(i2c,address=0x20)
for pin in range(npins):
    pin0 = mcp.get_pin(pin)
    pin0.direction = digitalio.Direction.OUTPUT
    pin0.pull = digitalio.Pull.UP
    pin0.value = False

app = FastAPI()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(inpin,GPIO.IN)
GPIO.setup(outpin,GPIO.OUT)

def pinstate():
    state = {}
    for pin in range(npins):
        pin0 =  mcp.get_pin(pin)
        state[pin] = pin0.value
    return state

@app.get("/")
def read_root():
    return {f'GPIO{inpin}': GPIO.input(inpin)}


@app.get("/on/{pinid}")
def pin_on(pinid: int, q: Optional[str] = None):
    if (pinid >= 0) & (pinid < npins):
        pin0 = mcp.get_pin(pinid)
        pin0.value = True
    return pinstate()
    
@app.get("/off/{pinid}")
def pin_off(pinid: int, q: Optional[str] = None):
    if (pinid >= 0) & (pinid < npins):
        pin0 = mcp.get_pin(pinid)
        # pin0.direction = digitalio.Direction.OUTPUT
        pin0.value = False
    return pinstate()


@app.get("/alloff")
def all_off():
    for pin in range(npins):
        pin0 =  mcp.get_pin(pin)
        pin0.value = False
    return pinstate()

@app.get("/allon")
def all_on():
    for pin in range(npins):
        pin0 =  mcp.get_pin(pin)
        pin0.value = True
    return pinstate()