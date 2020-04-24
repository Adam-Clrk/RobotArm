#!/usr/bin/env python3
import json
import asyncio
import websockets
from controllers import ArmController

MOTORS = ('base','shoulder','elbow','wrist','grip')

arm = ArmController()

async def echo(websocket, path):
  async for message in websocket:
    data = json.loads(message)
    print(data)
    if data['motor'] == 'all' and data['value'] == 0 :
      for motor in MOTORS:
        arm.arm.moveMotor(motor, 0)
    elif data['motor'] in MOTORS and isinstance(data['value'], int):
      arm.arm.moveMotor(data['motor'], data['value'])
    await websocket.send(message)
server = websockets.serve(echo, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()