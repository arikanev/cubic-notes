import numpy as np

v1 = [np.random.randint(-1,2) for i in range(3)]
v2 = [np.random.randint(-1,2) for i in range(3)]

v = [v1, v2]


def i2pv(N, p):

    v = []

    i = 0

    while p**i < abs(N):

        v.append(N % p**i)

        i += 1


    if len(v) == 0:

        v.append(0)

        return v

    return v


def addfr(v):

    if v[0][3] == v[1][3]:

        return add([v[0][:-1], v[1][:-1]]), v[0][3]

    elif v[0][3] < v[1][3]:

        return add([shift(*v[0][:-1], v[1][3] - v[0][3]), v[1][:-1]]), v[1][3]

    elif v[0][3] > v[1][3]:

        return add([shift(*v[1][:-1], v[0][3] - v[1][3]), v[0][:-1]]), v[0][3]


def shiftfr(a, b, c, i, j):

    if j == 0:

        return a, b, c, i

    elif j == 1:

        return 0, a, b, j + i

    elif j == 2:

        return 0, 0, a, i + j

    elif j == 3:

        return 0, 0, 0, i + j


def shift(a, b, c, j):

    if j == 0:

        return a, b, c

    elif j == 1:

        return 0, a, b

    elif j == 2:

        return 0, 0, a

    elif j == 3:

        return 0, 0, 0


def inversefr(a, b, c, i):

    return inverse(a, b, c), -i


def inverse(a, b, c):

    if a == 0:

        raise ValueError("divisible by p")

    elif a == 1:

        return normal(1, -b, -c + b**2)

    elif a == -1:

        return normal(-1, -b, c + b**2)

def normal(a, b, c):

    if abs(a) < 2:

        return a, mod3(b), mod3(c)

    elif a == 2:

        return -1, mod3(b), mod3(c - 1)

    elif a == -2:

        return 1, mod3(b), mod3(c + 1)

def mod3(a):

    return -1 if a % 3 == 2 else a % 3


def add(v):

    v3 = []

    for a, b in zip(v[0],v[1]):

        v3.append(mod3(a + b))

    return normal(v3[0], v3[1], v3[2])


def mul(v):

    return [normal(mod3(v[0][0] * v[1][0]), mod3(v[0][0] * v[1][1] + v[0][1] * v[1][0]), mod3(v[0][0] * v[1][2] + v[0][1]*v[1][1] + v[0][2] * v[1][0]))]

