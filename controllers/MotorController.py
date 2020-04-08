import time
from math import copysign

from .states import MotorState
from .ActuatorController import ActuatorController

class MotorController(ActuatorController):
  def __init__(self, motorName, movementFactor,state):
    self.state = MotorState(state)
    self.motorName = motorName
    self.movementFactor = movementFactor
    if hasattr(movementFactor, '__getitem__'):
      self.forwardMovementFactor = movementFactor[0]
      self.backwardMovementFactor = movementFactor[1]
    else:
      self.forwardMovementFactor = self.backwardMovementFactor = self.movementFactor
  def move_to(self, angle):
    """Move the motor from its current position to new angle

    Arguments:
      angle: float of new angle to move to
    """
    self.move_by(angle-self.state.angle)
  def move_by(self, angle):
    """Move the motor from its by an angle

    Arguments:
      angle: float of angle to move by
    """
    direction = int(copysign(1,angle))
    if direction != 0:
      movementFactor = self.forwardMovementFactor if direction > 0 else -self.backwardMovementFactor
      self.armController.moveMotor(self.motorName, direction)
      time.sleep(movementFactor*angle)
      # self.armController.moveMotor(self.motorName, 0)
      self.armController.stopMotor(self.motorName)
      self.state.angle += angle