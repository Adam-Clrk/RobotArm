#!/usr/bin/env python3
# Example file for testing the OWI Robotic Arm
# For use with RobotArm.py
#
# (C) Matt Dyson 2013
# http://mattdyson.org/projects/robotarm

import time
import json
import asyncio
import websockets

from controllers import ArmController
arm = ArmController()
# arm.timeTest()
def clicked(a):
  print('clicked',a)
  arm.arm.moveElbow(1)
  time.sleep(0.1)
  arm.arm.moveElbow(0)

MOTORS = ('base','shoulder','elbow','wrist','grip')
async def echo(websocket, path):
  async for message in websocket:
    data = json.loads(message)
    print(data)
    if data['motor'] in MOTORS and isinstance(data['value'], int):
      arm.arm.moveMotor(data['motor'], data['value'])
    await websocket.send(message)

server = websockets.serve(echo, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()