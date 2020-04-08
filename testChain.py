from KinematicChain import Coord3D, ArmChain, Coord3D
from math import radians, pi

# a = Coord3D.from_cylindrical_about_y(1,1,radians(90))
# print(a)
# print([round(b,5) for b in a.loc])
ARM_SEGMENT_LENGTHS = {
  'ab': 6.5e-2,
  'bc': 9.0e-2,
  'cd': 6.2e-2,
  'de': 1.15e-1
}
a = ArmChain(ARM_SEGMENT_LENGTHS)

angles_list = [
  (0,0,0,0),
  (0.2*(2*pi),0,0,0),
  (radians(0),0,radians(10),0),
  (0,0,0,radians(45))
]
for angles in angles_list:
  print('======')
  loc = [round(loc,10) for loc in a.resolve_forward(angles).loc]
  newangles = a.resolve_inverse(loc)
  print(angles, loc, newangles)

resolved_angles = a.resolve_inverse(Coord3D((1,1,1)))
print(resolved_angles)