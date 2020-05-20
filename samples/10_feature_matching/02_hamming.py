import numpy as np


def main():

    # A = int("1111", 2)
    # B = int("0011", 2)

    A = 0b1111
    B = 0b0011

    C = np.bitwise_xor(A, B)

    print("A: {}, B: {}".format(A, B))
    print("XOR(A, B): {:4b}".format(C))

    # Hamming distance

    count = 0
    while (C != 0):

        C = C & (C - 1)
        count += 1

    print("D:{}".format(count))

    return


if __name__ == "__main__":

    main()
