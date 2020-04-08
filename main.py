from controllers import StatefulArmController, MotorController, LEDController
from math import radians
import time
# statefulArmController = StatefulArmController([
#   MotorController('base',1),
#   MotorController('shoulder',1),
#   MotorController('elbow',1),
#   MotorController('wrist',1),
#   MotorController('grip',1),
#   LEDController()
# ])
# help(statefulArmController)

statefulArmController = StatefulArmController([
  MotorController('base',4.065232667779,radians(-20)),
  MotorController('shoulder',(4.068371018277, 7.681479359482),0)
])
base = statefulArmController.controllers[0]
shoulder = statefulArmController.controllers[1]
# c.move_by(radians(-45))
# c.move_by(radians(45))
# time.sleep(1)
# c.move_by(radians(90))
# c.move_by(radians(-90))
# for i in range(90):
#   c.move_by(radians(1))
# time.sleep(5)
# c.move_by(radians(-90))
for i in range(2):
  base.move_to(radians(20))
  print('1')
  time.sleep(1)
  base.move_to(radians(0))
  print('2')
  time.sleep(1)
  base.move_to(radians(-20))
  print('3')
  time.sleep(1)
  # shoulder.move_to(radians(-20))
  # time.sleep(1)
  # shoulder.move_to(radians(0))
  # time.sleep(1)
base.move_to(radians(0))
del statefulArmController.arm