# Limitations: no roll, each joint can only have one axis of rotation

class KinematicChain():
  def __init__(self, lengths):
    """represents a kinematic chain
    Args:
      lengths: dictionary of lengths in chain
    """
    self.lengths = lengths
    self.n_joints = len(lengths)
    pass

from math import sin, cos, degrees, radians,pi

class CoordBase:
  def __init__(self, loc):
    """init coordinate
    Args:
      loc: tuple of current position of the coordinate
    """
    self.loc = loc
  def __repr__(self):
    return str(self.loc)

class Coord2D(CoordBase):
  def __init__(self, loc):
    super().__init__(loc)
  @classmethod
  def from_polar(cls,r,theta):
    # a = (r*cos(theta),r*sin(theta))
    return cls((r*cos(theta),r*sin(theta)))
  @classmethod
  def from_polar_degrees(cls,r,theta):
    return cls((r*cos(radians(theta)),r*sin(radians(theta))))
  @property
  def x(self):
    return self.loc[0]
  @property
  def y(self):
    return self.loc[1]
  def __add__(self, other):
    return self.__class__((self.x+other.x,self.y+other.y))

class Coord3D(CoordBase):
  def __init__(self,loc):
    super().__init__(loc)
  @classmethod
  def from_cylindrical_about_y(cls, x, y, theta):
    return cls((x*cos(theta),y,x*sin(theta)))

from math import sqrt, asin

class ArmChain(KinematicChain):
  def resolve_forward(self, angles):
    """resolve location of end of chain from angles
    Args:
      angles: tuple of the joint external angles in radians
    """
    assert self.n_joints == len(angles) # should be 4
    L = self.lengths
    a = Coord2D((0,0))
    b = a + Coord2D((0,L['ab']))
    c = b + Coord2D.from_polar(L['bc'],-angles[1]+(0.5*pi))
    d = c + Coord2D.from_polar(L['cd'],-angles[2]+(0.5*pi))
    e = d + Coord2D.from_polar(L['de'],-angles[3]+(0.5*pi))
    # e = Coord2D((0,0)) + Coord2D((0,L['ab'])) + Coord2D.from_polar(L['bc'],angles[1]) + Coord2D.from_polar(L['cd'],angles[2]) + Coord2D.from_polar(L['de'],angles[3])
    e_3d = Coord3D.from_cylindrical_about_y(e.x,e.y,angles[0])
    return e_3d

  def resolve_inverse(self, end):
    angles = [0,0,0,0,0]
    x,y,z = end
    # first work out rotation of a, leaving us with a 2d problem
    rho = sqrt(x**2+z**2)
    phi = 0 if x==0 and z==0 else (asin(y/rho) if x >= 0 else None)
    # phi = rotation of a
    assert not phi == None
    angles[0] = phi
    loc_2d = Coord2D((rho,y))
    print(loc_2d)

    return tuple(angles)


# a = Coord2D((0,0))
# b = a + Coord2D((0,ARM_SEGMENT_LENGTHS['ab']))
# c = b + Coord2D.from_polar_degrees(ARM_SEGMENT_LENGTHS['bc'],90)
# d = c + Coord2D.from_polar_degrees(ARM_SEGMENT_LENGTHS['cd'],90)
# e = d + Coord2D.from_polar_degrees(ARM_SEGMENT_LENGTHS['de'],0)
# print(e)
# L = ARM_SEGMENT_LENGTHS
# e = Coord2D((0,0)) + Coord2D((0,L['ab'])) + Coord2D.from_polar_degrees(L['bc'],90) + Coord2D.from_polar_degrees(L['cd'],90) + Coord2D.from_polar_degrees(L['de'],0)
# print(e)

a = Coord2D((0,0))
# for segment in segments:
  # segment