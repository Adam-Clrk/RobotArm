class ActuatorState:
  """Generic class representing the state of an actuator
  Attributes:
    instant: A boolean indicating if a change in state can be done instantly
    changing: A boolean indicating if the actuator is currently changing state
    ready: A boolean indicating if the acuator is ready for a new instruction
  """
  def __init__(self, instant=True):
    """
    Args:
      instant: A boolean indicating if a change in state can be done instantly
    """
    self.instant = instant
    self.changing = False
    self.ready = False
  def set_ready(self):
    """Mark the actuator as ready for changes in state"""
    self.ready = True
  @property
  def is_availiable(self):
    return self.ready and not self.changing
  def start_changing(self):
    """Mark the actuator as currently changing"""
    if not self.instant:
      self.changing = True
  def done_changing(self):
    """Mark the actuator as finished changing"""
    self.changing = False
  def change(self,state):
    self.start_changing()
    self.done_changing()

class MotorState(ActuatorState):
  """Represents the current state of a motor"""
  def __init__(self, angle):
    super().__init__(instant=False)
    self.angle = angle


class LEDState(ActuatorState):
  """Represents the current state of an LED"""
  def __init__(self):
    super().__init__()
    self.is_on = False
  def set_on(self):
    """Mark the LED as on"""
    self.is_on = True
  def set_off(self):
    """Mark the LED as off"""
    self.is_on = False
  def toggle(self):
    """Toggle LED state
    Returns:
      Boolean of new LED state
    """
    self.is_on = not self.is_on
    return self.is_on
  @property
  def state(self):
    return self.is_on