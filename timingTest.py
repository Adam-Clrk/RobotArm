#!/usr/bin/env python3
# Example file for testing the OWI Robotic Arm
# For use with RobotArm.py
#
# (C) Matt Dyson 2013
# http://mattdyson.org/projects/robotarm


import tkinter
import time
import json
import asyncio
import websockets

from controllers import ArmController
arm = ArmController()

MOTORS = ('base','shoulder','elbow','wrist','grip')

import time


for motor in MOTORS:
  print(f'testing motor: {motor}')
  input('Enter to start')
  arm.arm.moveMotor(motor, 1)
  start_time = time.time()
  input('Enter to stop')
  print("--- %s seconds ---" % (time.time() - start_time))
  arm.arm.moveMotor(motor, 0)
  input('Enter to reverse')
  start_time = time.time()
  arm.arm.moveMotor(motor, 2)
  input('Enter to stop')
  print("--- %s seconds ---" % (time.time() - start_time))
  arm.arm.moveMotor(motor, 0)
  