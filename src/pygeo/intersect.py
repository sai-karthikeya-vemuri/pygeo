from .objects import Ray, Sphere, Triangle
import numpy as np

def intersect(first_object, second_object):
    if isinstance(first_object,Ray):
        if isinstance(second_object,Sphere):
            val=_intersect_ray_with_sphere(first_object, second_object)
        elif isinstance(second_object,Triangle):
            val= _intersect_ray_with_triangle(first_object, second_object)
        return val
    else:
        return f"NotImplemented"



def _intersect_ray_with_sphere(ray, sphere):
    l=(ray._direction - ray._origin)/np.linalg.norm(ray._direction - ray._origin)
    o=ray._origin
    c=sphere._center
    r=sphere._radius
    delta = ((np.dot(l,o-c))**2)-(((np.linalg.norm(o-c))**2)-(r**2))
    if delta < 0 :
        return 0
    if delta == 0:
        d = (-1*np.dot(l,o-c))
        return [o+(d*l)]
    if delta > 0 :
        d1 = (-1*np.dot(l,o-c)) + np.sqrt(delta)
        d2 = (-1*np.dot(l,o-c)) - np.sqrt(delta)
        return [o+(d1*l),o+(d2*l)]



def _intersect_ray_with_triangle(ray, triangle):
    u = triangle._point2-triangle._point1
    v = triangle._point3-triangle._point1
    normal = np.cross(u, v)
    p0=ray._origin
    p1=ray._direction
    b = np.inner(normal, p1 - p0)
    a = np.inner(normal, triangle._point1 - p0)
    if (b == 0.0):
        if a != 0.0:
            return 0
        else:
            rI = 0.0
    else:
        rI = a / b
    if rI < 0.0:
        return 0  
    w = p0 + rI * (p1 - p0) - triangle._point1  
    denom = np.inner(u, v) * np.inner(u, v) - \
        np.inner(u, u) * np.inner(v, v)
    si = (np.inner(u, v) * np.inner(w, v) - \
        np.inner(v, v) * np.inner(w, u)) / denom
    if (si < 0.0) | (si > 1.0):
        return 0
    ti = (np.inner(u, v) * np.inner(w, u) - \
        np.inner(u, u) * np.inner(w, v)) / denom
    
    if (ti < 0.0) | (si + ti > 1.0):
        return 0
    if (rI == 0.0):
        return 2
    return 1