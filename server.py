#!/usr/bin/env python

import web
import json
import wiringpi2
import time
import mido
import signal

## Setup
######################################################
io = wiringpi2.GPIO(wiringpi2.GPIO.WPI_MODE_PINS)

io.pinMode(4, io.OUTPUT)

app = web.auto_application()

render = web.template.render('templates/')


def pulse(duration):
  io.digitalWrite(4, io.LOW)
  time.sleep(duration)
  io.digitalWrite(4, io.HIGH)

def pause(duration):
  time.sleep(duration)


## Routes
######################################################
class index(app.page):
  path = "/"
  def GET(self):
    return render.index()

class switch(app.page):
  path = "/switch"

  def POST(self):
    i = web.input()

    state = i.state

    if state == 'on':
      io.digitalWrite(4, io.LOW)

    if state == 'off':
      io.digitalWrite(4, io.HIGH)


class flicker(app.page):
  path = "/flicker"

  def POST(self):
    i = web.input()

    d = float(i.time)

    for x in range(0, 5):
      pulse(d)
      pause(d)
      pulse(d)
      pause(d)
      pulse(d)
      pause(d)


class midi(app.page):
  path = "/midi"

  def POST(self):
    i = web.input()

    mid = mido.MidiFile(i.filename)

    for msg in mid.play():
      if msg.channel is 9:
        if hasattr(msg, 'velocity') is True:
          if msg.velocity is 100:
            io.digitalWrite(4, io.LOW)
          if msg.velocity is 0:
            io.digitalWrite(4, io.HIGH)


## Run
######################################################
app.run()
