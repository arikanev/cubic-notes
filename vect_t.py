import itertools

comb = itertools.product([i for i in range(-4, 5)], repeat=4)

for a,b,c,d in comb:

    if sum([abs(a),abs(b),abs(c),abs(d)]) == 0:

        with open('vints.txt', 'a') as f:

            f.write('{} {} {} {}'.format(a,b,c,d))
