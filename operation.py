import numpy as np

v1 = [np.random.randint(-1,2) for i in range(3)]
v2 = [np.random.randint(-1,2) for i in range(3)]

v = [v1, v2]


def mod3(a):

    return -1 if a % 3 == 2 else a % 3


def padd(v):

    v3 = []

    for a, b in zip(v[0],v[1]):

        v3.append(mod3(a + b))

    return v3


def pmul(v):

    return [mod3(v[0][0] * v[1][0]), mod3(v[0][0] * v[1][1] + v[0][1] * v[1][0]), mod3(v[0][0] * v[1][2] + v[0][1]*v[1][1] + v[0][2] * v[1][0])]
