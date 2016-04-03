#!/bin/python

import os
import sys
import getopt
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "sensor")))
from sensor import Sensor:x

port_a = 40
port_b = 37

motion_detector = Sensor(idle_timeout = 5)
motion_detector.add_listener(port_a, "TeamA")
motion_detector.add_listener(port_b, "Team B")


global user_input
while user_input not "quit":
    user_input=raw_input("type 'quit' to exit")
