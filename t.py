import math
import numpy as np
import itertools

def is_coprime(y0,y1,z0,z1,u0,u1):

    return math.gcd(y0,y1,z0,z1,u0,u1) == 1

def form(y0,y1,z0,z1,u0,u1):

    def mul(ab, c, d):

        a, b = ab

        return a*c - b*d, b*c + a*d - b*d

    def add(ab, c, d):

        a, b = ab

        return a + c, b + d

    _y0, _y1 = mul(mul((y0, y1), y0, y1), y0, y1)
    _z0, _z1 = mul(mul((z0, z1), z0, z1), z0, z1)
    _u0, _u1 = mul(mul(mul((u0, u1), u0, u1), u0, u1), 0, 1)

    return add(add((_y0, _y1), _z0, _z1), _u0, _u1)

comb = itertools.product([i for i in range(-20,21)], repeat=6)

for y0,y1,z0,z1,u0,u1 in comb:

    if is_coprime(y0,y1,z0,z1,u0,u1):

        if np.array_equal(np.array([1, 0]) + np.array(form(y0,y1,z0,z1,u0,u1)), np.array([0,0])):

            with open('ints.txt', 'a') as f:

                f.write('{} {} {} {} {} {}\n'.format(y0,y1,z0,z1,u0,u1))
