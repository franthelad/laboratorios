'''
Scenario
Now we're going to embed the Point class (see Lab 3.4.1.14) inside another
class. Also, we're going to put three points into one class, which will let us
define a triangle. How can we do it?

The new class will be called Triangle and this is the list of our expectations:


the constructor accepts three arguments - all of them are objects of the Point
class;

the points are stored inside the object as a private list;

the class provides a parameterless method called perimeter(), which calculates
the perimeter of the triangle described by the three points; the perimeter is
a sum of all legs' lengths (we mention it for the record, although we are sure
that you know it perfectly yourself.)
'''

import math


class Point:
    
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y 


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):

        self.__triangle = [vertice1, vertice2, vertice3]

        self.__side1 = math.hypot(abs(vertice1.getx() - vertice2.getx()), abs(vertice1.gety() - vertice2.gety()))
        self.__side2 = math.hypot(abs(vertice2.getx() - vertice3.getx()), abs(vertice2.gety() - vertice3.gety()))
        self.__side3 = math.hypot(abs(vertice3.getx() - vertice1.getx()), abs(vertice3.gety() - vertice1.gety()))
        
    def perimeter(self):
        
        return self.__side1 + self.__side2 + self.__side3
    
triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
