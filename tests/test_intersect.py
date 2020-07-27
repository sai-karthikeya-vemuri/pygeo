from pygeo.intersect import (
    intersect,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
from pygeo.objects import Ray, Sphere, Triangle

import numpy as np
# intersect



def test__intersect_ray_with_sphere_return_true():
    sph = Sphere((0,0,0),1)
    ray =Ray((-1,0,0),(0,0,0))
    temp = _intersect_ray_with_sphere(ray,sph)
    val=1
    print(temp)
    if np.array_equal(temp,[[1.0,0.0,0.0],[-1.0,0.0,0.0]]):
        val=2
    assert (val == 2) is True

def test__intersect_ray_with_sphere_return_false():
    sph = Sphere((0,0,0),1)
    ray =Ray((1,0,0),(1,1,0))
    val=2
    temp = _intersect_ray_with_sphere(ray,sph)
    print(temp)
    if np.array_equal(temp,[[1.0,0.0,0.0]]) is True:
        val=1
    
    
    assert (val == 2) is False
def test__intersect_ray_with_sphere_return_true_1():
    sph = Sphere((0,0,0),2)
    ray =Ray((2,0,0),(2,1,0))
    temp = _intersect_ray_with_sphere(ray,sph)
    val=2
    if np.array_equal(temp,[[2,0,0]]) is True:
        val=1
    assert (val == 1) is True

def test__intersect_ray_with_sphere_return_false_1():
    sph = Sphere((0,0,0),1)
    ray =Ray((5,0,0),(0,5,0))
    val=2
    temp = _intersect_ray_with_sphere(ray,sph)
    if temp==0:
        val=0
    assert (val == 2) is False
def test__intersect_ray_with_triangle_return_true():
    triangle=Triangle((1,0,0),(-1,0,0),(0,1,0))
    ray= Ray((1,0,1),(-1,0,1))
    val = _intersect_ray_with_triangle(ray, triangle)
    assert (val==0) is True
def test__intersect_ray_with_triangle_return_false():
    triangle=Triangle((1,0,0),(-1,0,0),(0,1,0))
    ray= Ray((0.5,0,0),(0,0.5,0))
    val = _intersect_ray_with_triangle(ray, triangle)
    assert (val==0) is False
def test__intersect_ray_with_triangle_return_true_1():
    triangle=Triangle((1,0,0),(-1,0,0),(0,1,0))
    ray= Ray((0.5,0,0),(0,0.5,0))
    val = _intersect_ray_with_triangle(ray, triangle)
    assert (val==2) is True
def test__intersect_ray_with_triangle_return_false_2():
    triangle=Triangle((1,0,0),(-1,0,0),(0,1,0))
    ray= Ray((0,0,1),(0,0,0))
    val = _intersect_ray_with_triangle(ray, triangle)
    assert (val==0) is False