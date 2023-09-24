"""Write a Polyline class that uses the Point3d class and can return the length of the polyline
"""
import random
import math
import matplotlib.pyplot as plt

def display_pl(polyline):
    xs, ys = [], []
    for pt in polyline.points:
        xs.append(pt.x)
        ys.append(pt.y)
    plt.plot(xs,ys)

class Point3d():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    @property
    def data(self):
        return (self.x,self.y,self.z)

# Create class here
class Polyline():
    
    def __init__(self, *points1):
        self.points = []
        for point in points1:
            self.points.append(point)
    def length(self):
        length_polyline = 0
        for i in range(len(self.points)-1):
            length_polyline += math.sqrt(math.pow(self.points[i].data[1]-self.points[i+1].data[1],2) + math.pow(self.points[i].data[0]-self.points[i+1].data[0],2))
        return length_polyline


point1 = Point3d(3,4,5)
point2 = Point3d(1,1,1)
polyline = Polyline(point1, point2)# Create object based on class Polyline here
polyline_length = polyline.length# Polyline length class method function here
print(polyline_length)
plt.figure()
display_pl(polyline)
plt.show()