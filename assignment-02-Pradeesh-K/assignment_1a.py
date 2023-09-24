"""
1a. Given two vectors, use the cross product to create a set of three orthonormal vectors.
"""

from compas.geometry import cross_vectors
from compas.geometry import angle_vectors
import math as m


v1 = [1, 2, 3]
v2 = [4, 5, 6]

#making them orthogonal
x1 = cross_vectors(v1, v2)  # = # Orthonormal vector 1
x2 = [-x1[1], x1[0], 0]     # = # Orthonormal vector 2
x3 = cross_vectors(x1, x2)  # = # Orthonormal vector 3

#making them normal
mod = m.sqrt(x1[0] ** 2+x1[1] ** 2 + x1[2] ** 2)
x1 = [round(i*(1/mod),2) for i in x1]
mod = m.sqrt(x2[0] ** 2+x2[1] ** 2 + x2[2] ** 2)
x2 = [round(i*(1/mod),2) for i in x2]
mod = m.sqrt(x3[0] ** 2+x3[1] ** 2 + x3[2] ** 2)
x3 = [round(i*(1/mod),2) for i in x3]
print(x1)
print(x2)
print(x3)



print(round(m.degrees(angle_vectors(x1, x2))))
print(round(m.degrees(angle_vectors(x1, x3))))
print(round(m.degrees(angle_vectors(x2, x3))))
