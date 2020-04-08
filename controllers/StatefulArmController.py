from .ArmController import ArmController

DIRECTION_MAP = {
  -1: 2,
  0: 0,
  1: 1
}

class StatefulArmController(ArmController):
  """Holds stateful controllers for all the motors/LEDs in  the arm.
  
  Attributes:
    controllers: list of controllers (all child classes of ActuatorController)
  """

  def __init__(self, controllers):
    """
    initiate class

    Args:
      controllers: list of controllers
    """
    super().__init__()
    self.controllers = controllers
    for controller in self.controllers:
      # self.controllers[controller]._set_arm(self.arm)
      # self.controllers[controller]._set_armController(self)
      controller._set_armController(self)
  def moveMotor(self, motor, direction):
    """Starts a motor moving in a specified direction

    Args:
      motor: string identifying which motor is being controlled
      direction: integer -1, 0 or 1 specifying the direction
    """
    direction = DIRECTION_MAP[direction]
    self.arm.moveMotor(motor, direction)
  def stopMotor(self, motor):
    """Stops a specified motor

    Args:
      motor: string identifying which motor is being stopped
    """
    self.arm.moveMotor(motor, 0)
  def setLed(self, state):
    self.arm.setLight(int(state))
