#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Andrea
#
# Created:     14/03/2015
# Copyright:   (c) Andrea 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
class Vector(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Point(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def dot_product(vector1, vector2):
    return vector1.x * vector2.x + vector1.y * vector2.y + vector1.z * vector2.z

def cross_product(vector1, vector2):
    i = vector1.y * vector2.z - vector1.z * vector2.y
    j = vector1.z * vector2.x - vector1.x * vector2.z
    k = vector1.x * vector2.y - vector1.y * vector2.x
    return Vector(i, j, k)

def convert_to_polar_coords(point):
    z = point.z
    r = math.sqrt(point.x ** 2 + point.y ** 2)
    theta = math.atan(point.y / point.x)
    return Point(r, theta, z)

def convert_to_spherical(cartesian_point):
    polar_point = convert_to_polar_coords(cartesian_point)
    rho = math.sqrt(polar_point.x ** 2 + polar_point.z ** 2)
    phi = math.acos(polar_point.z / rho)
    theta = polar_point.y
    return Point(rho, phi, theta)

def convert_from_polar(polar_point):
    z = polar_point.z
    y = polar_point.x * math.cos(polar_point.y)
    x = polar_point.x * math.sin(polar_point.y)
    return Point(x, y, z)

def convert_to_spherical(spherical_point):
    rho = spherical_point.x
    phi = spherical_point.y
    theta = spherical_point.z
    x = rho * math.sin(phi) * math.cos(theta)
    y = rho * math.sin(phi) * math.sin(theta)
    z = rho * math.cos(phi)
    return Point(x, y, z)



def main():
    vect_1 = Vector(2, 3, 2)
    vect_2 = Vector(3 , 2, 3)
    print dot_product(vect_1, vect_2)
    c_prdct = cross_product(vect_1, vect_2)
    print c_prdct.x, c_prdct.y, c_prdct.z

if __name__ == '__main__':
    main()
