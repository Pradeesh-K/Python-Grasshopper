"""
1b. Use the cross product to compute the area of a convex, 2D polygon with more than 3 sides.
"""

from compas.geometry import Vector
from compas.geometry import area_polygon

#Input points
a = [1,1,0]#...
b = [4,2,0]#...
c = [5,3,0]#...
# additional points
polygon = [a,b,c,[3,5,0],[1,7,0]] # add additional points here

ab = Vector.from_start_end(a,b)#Vector1
ac = Vector.from_start_end(a,c)#Vector2
# additional vectors
ad = Vector.from_start_end(a,[3,5,0])
ae = Vector.from_start_end(a,[1,7,0])
#Calculate area
A = (ab.cross(ac).length + ac.cross(ad).length +ad.cross(ae).length)* 0.5 #Area

# Display area
print(A)

# Area as computed by the area_polygon function of compas
A2 = round(area_polygon(polygon))       #rounded up the decimal values
print(A2)
#and check your result
print("Area correct:", A == A2)


