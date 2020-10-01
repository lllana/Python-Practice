# The surface of the Earth is curved, and the distance between degrees of 
# longitude varies with latitude. As a result, finding the distance between two points on the surface
# of the Earth is more complicated than simply using the Pythagorean theorem.
# Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on
# the Earth’s surface. The distance between these points, following the surface of the Earth, 
# in kilometers is:
# distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))

import math 

t1 = math.radians(int(input("Hi! Insert latitude of the first point ....")))
g1 = math.radians(int(input("Insert longitude of the first point ....")))

t2 = math.radians(int(input("Insert latitude of the second point ....")))
g2 = math.radians(int(input("Insert longitude of the second point ....")))

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) * math.cos(t1) * math.cos(t2) * math.cos(g1-g2))

print("The distance is {} kilometers". format(distance))