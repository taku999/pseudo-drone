#!/bin/env python
# -*- coding: utf-8 -*-
import json
import time

import random
import datetime

import tornado.websocket
import tornado.web
import tornado.ioloop

#import RPi.GPIO as GPIO

import sys

# initialize GPIO
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

# read data using pin no
#instance = dht11.DHT11(pin=4)

file_path = './test.json'

class SendWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('Session Opened. IP:' + self.request.remote_ip)
        self.ioloop = tornado.ioloop.IOLoop.instance()

        self.send_websocket()

    def on_close(self):
        print("Session closed")

    def check_origin(self, origin):
        return True

    def send_websocket(self):
        self.ioloop.add_timeout(time.time() + 1, self.send_websocket)
        if self.ws_connection:
            if True:
            #if(result.is_valid()):                
                with open(file_path, "r") as json_file:
                    result = json.load(json_file)
                print(result)
                message = json.dumps({
                    #'time': result['Time'],
                    #'Temperature': result['g1']['Temperature'],
                    #'Humidity': result['g1']['Humidity'],
                    'time': result['Time'],
                    'g1':{
                        'SW'  : result['g1']['SW'],
                        'RSSI': result['g1']['RSSI'],
                        'Volt': result['g1']['Volt'],
                        'Long': result['g1']['Long'],
                        'Lat' : result['g1']['Lat'],
                        'Temperature': result['g1']['Temperature'],
                        'Humidity': result['g1']['Humidity']
                    }
                })
                self.write_message(message)
                time.sleep(5)


app = tornado.web.Application([(r"/ws/display", SendWebSocket)])

if __name__ == "__main__":
    app.listen(9001,'192.168.0.117')
    tornado.ioloop.IOLoop.current().start()