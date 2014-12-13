#!/usr/bin/env python

import web
import json
import wiringpi2
import time

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

      web.header('Content-Type', 'application/json')

      return json.dumps({"response" : "ok"})

class dance(app.page):
    path = "/dance"

    def POST(self):
      i = web.input()

      d = float(i.time)

      for x in range(0, 5):
        pulse(d)
        pause(d)
        pulse(d)
        pause(d)
        pulse(d)
        pause(1)

      web.header('Content-Type', 'application/json')

      return json.dumps({"response" : "ok"})

## Run
######################################################
if __name__ == "__main__":
  app.run()