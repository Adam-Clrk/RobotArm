from armcontrol import RobotArm
from usb import core as usbcore
import time

VENDOR = 0x1267
PRODUCT = 0x0000
class ArmController:
  """
  Arm controller which manages the whole arm, with no state

  Attributes:
    self.arm: RobotArm instance
  """
  def __init__(self):
    try:
      dev = usbcore.find(idVendor=VENDOR, idProduct=PRODUCT)
      if dev == None:
        print('Robot arm not plugged in')
      else:
        dev.get_active_configuration()
        self.arm = RobotArm.RobotArm()
    except usbcore.USBError as e:
      if e.errno == 13:
        print(f'Init failed, try running:\n\tsudo chmod o+rw /dev/bus/usb/{dev.bus:03}/{dev.address:03}')
      raise e
  def test(self):
    try:
      print("Moving elbow")
      self.arm.moveElbow(1)
      time.sleep(1)

      print("Moving wrist as well")
      self.arm.moveWrist(1)
      time.sleep(1)

      print("Moving base as well")
      self.arm.moveBase(2)
      time.sleep(3)

      print("Stopping")
      self.arm.reset()

      print("Moving elbow back")
      self.arm.moveElbow(2)
      time.sleep(1)

      print("Moving wrist back as well")
      self.arm.moveWrist(2)
      time.sleep(1)

      print("Moving base back as well")
      self.arm.moveBase(1)
      time.sleep(3)
    finally:
      self.arm.reset()