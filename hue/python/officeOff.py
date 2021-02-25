#!/usr/bin/python

from phue import Bridge

b = Bridge('192.168.1.142')

for light in b.lights:
    if light.name == 'Office':
        light.on = False

    if light.name == 'Office Floor Lamp':
        light.on = False
