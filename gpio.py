#!/usr/bin/env python

import wiringpi2
import time

pin = {
  17 : 0,
  18 : 1,
  23 : 4
}

io = wiringpi2.GPIO(wiringpi2.GPIO.WPI_MODE_PINS)

io.pinMode(pin[17], io.OUTPUT)
io.pinMode(pin[18], io.OUTPUT)
io.pinMode(pin[23], io.OUTPUT)

def setInterval(interval = .5):
  interval = interval

def flash(pin, interval):
  io.digitalWrite(pin, io.HIGH)
  time.sleep(interval)
  io.digitalWrite(pin, io.LOW)

def switch(pinNum, state):
  if state == 'on':
    io.digitalWrite(pin[pinNum], io.HIGH)

  if state == 'off':
    io.digitalWrite(pin[pinNum], io.LOW)

  print io.digitalRead(pin[pinNum])