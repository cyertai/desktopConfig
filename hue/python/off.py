#!/usr/bin/python

from phue import Bridge

b = Bridge('192.168.1.142')

#print(b.connect())

#print(b.get_api())

lights = b.lights

for light in lights:
    light.on = False
