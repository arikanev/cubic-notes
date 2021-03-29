import itertools

comb = itertools.product([i for i in range(-4, 5)], repeat=4)

for a,b,c,d in comb:

    T = 1 + complex(a,b)**3 + complex(c,d)**3 * complex(-1/2, (3**(1/2))/2)
    y1 = -(T ** (1/3)).real
    y2 = -(T ** (1/3)).imag

    m1 = round(y1)
    m2 = round(y2)

    if (y1 - m1) < 0.001 and (y2 - m2) < 0.001:

        if 1 + complex(m1, m2)**3 + complex(a,b)**3 + complex(c, d)**3 * complex(-(1/2), (3**(1/2))/2) == complex(0, 0):

            print(m1, m2, a, b, c, d)
