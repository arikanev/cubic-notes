import numpy as np

v1 = [np.random.randint(-1,2) for i in range(3)]
v2 = [np.random.randint(-1,2) for i in range(3)]

v = [v1, v2]

def padd_fr(v):

    

def pinverse_fr(a, b, c, i):

    a, b, c = inverse(a, b, c)

    return a, b, c, -i

def pinverse(a, b, c):

    if a == 0:

        raise ValueError("divisible by p")

    elif a == 1:

        return normal(1, -b, -c + b**2)

    elif a == -1:

        return normal(-1, -b, c + b**2)

def pnormal(a, b, c):

    if abs(a) < 2:

        return a, mod3(b), mod3(c)

    elif a == 2:

        return -1, mod3(b), mod3(c - 1)

    elif a == -2:

        return 1, mod3(b), mod3(c + 1)

def mod3(a):

    return -1 if a % 3 == 2 else a % 3


def padd(v):

    v3 = []

    for a, b in zip(v[0],v[1]):

        v3.append(mod3(a + b))

    return normal(v3[0], v3[1], v3[2])


def pmul(v):

    return [normal(mod3(v[0][0] * v[1][0]), mod3(v[0][0] * v[1][1] + v[0][1] * v[1][0]), mod3(v[0][0] * v[1][2] + v[0][1]*v[1][1] + v[0][2] * v[1][0]))]

