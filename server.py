#!/usr/bin/env python

import web
import json
import wiringpi2
import time

## Setup
######################################################
pins = {
  17 : 0,
  18 : 1,
  23 : 4
}

io = wiringpi2.GPIO(wiringpi2.GPIO.WPI_MODE_PINS)

io.pinMode(pins[17], io.OUTPUT)
io.pinMode(pins[18], io.OUTPUT)
io.pinMode(pins[23], io.OUTPUT)

app = web.auto_application()

render = web.template.render('templates/')


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

      pin   = int(i.pin)
      state = i.state

      #if state == 'on':
      io.digitalWrite(pins[pin], io.HIGH)
      time.sleep(1)
      #if state == 'off':
      io.digitalWrite(pins[pin], io.LOW)

      web.header('Content-Type', 'application/json')

      return json.dumps({"response" : "ok"})


## Run
######################################################
if __name__ == "__main__":
  app.run()