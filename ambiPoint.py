from Point import *
p1=Point()
p1.x=2
p1.y=4
p2=Point()
p2.set_location(3,4)
print(p2.x)
print(p2.distance_from_origin())
print(p2.distance(p1))
