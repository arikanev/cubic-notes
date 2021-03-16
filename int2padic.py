import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--int", "-n", type=int)
parser.add_argument("--prime", "-p", type=int)


args = parser.parse_args()


def padic2vector(N, p):

    v = []

    i = 0

    while p**i < abs(N):

        v.append(N % p**i)

        i += 1


    if len(v) == 0:

        v.append(0)

        return v

    return v


print(padic2vector(args.int, args.prime))

