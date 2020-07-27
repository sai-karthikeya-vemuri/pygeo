import numpy as np


class Point:
    """A point."""

    def __init__(self, point):
        self._point = np.array(point, dtype=float)

    def __repr__(self):
        return f"Point({self._point.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self._point + other._vector)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Point(other._vector + self._point)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self._point - other._point)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point):
            return np.array_equal(other._point, self._point)
        return False


class Vector:
    """A vector."""

    def __init__(self, vector):
        self._vector = np.array(vector, dtype=float)

    def __repr__(self):
        return f"Point({self._vector.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector + other._vector)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector - other._vector)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return np.array_equal(other._vector, self._vector)
        return False


class Ray:
    """A ray."""
    def __init__(self,origin,direction):
        self._origin=np.array(origin,dtype=float)
        self._direction=np.array(direction,dtype=float)
    def __repr__(self):
        return f"Origin:({self._origin.tolist()}) \n direction:({self._direction.tolist()})"
    def __eq__(self,other):
        if isinstance(other,Ray):
            return (np.array_equal(self._origin,other._origin) and  np.array_equal(other._direction==self._direction))
        return False


    ...


class Sphere:
    """A sphere."""
    def __init__(self,center,radius):
        self._center = np.array(center,dtype=float)
        self._radius = radius
    def __repr__(self):
        return f"Center:({self._center.tolist()}) \n radius:({self._radius})"
    def __eq__(self,other):
        if isinstance(other,Sphere):
            return (np.array_equal(self._center,other._center) and  (other._radius==self._radius))
        return False
        

    ...


class Triangle:
    """A triangle."""
    def __init__(self,point1,point2,point3):
        self._point1 = np.array(point1,dtype=float)
        self._point2 = np.array(point2,dtype=float)
        self._point3 = np.array(point3,dtype=float)
    def __repr__(self):
        return f"The triangle \n point1:({self._point1.tolist()}) \n point2:({self._point2.tolist()}) \n point3:({self._point3.tolist()})"
    def __eq__(self,other):
        if isinstance(other,Triangle):
            return (np.array_equal(self._point1,other._point1) and np.array_equal(self._point2,other._point2) and np.array_equal(self._point3,other._point3))
        return False


    
