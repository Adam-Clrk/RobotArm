from .ActuatorController import ActuatorController
from .states import LEDState

class LEDController(ActuatorController):
  def __init__(self):
    self.state = LEDState()
  def toggle(self):
    """Toggles LED"""
    new_state = self.state.toggle()
    if new_state:
      self.off()
    else:
      self.on()
  def on(self):
    """Turns LED on"""
    self.armController.setLight(True)
    self.state.set_on()
  def off(self):
    """Turns LED off"""
    self.armController.setLight(True)
    self.state.set_off()
