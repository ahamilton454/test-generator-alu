import random as r

def get_min_max():

    min = -2147483648
    max = 2147483647  # 2^32 - 1

    return min, max

def refit_to_32bit(val):
    min, max = get_min_max()

    if val > max:
        val = val - 2**32
    elif val < min:
        val = val + 2**32

    binary = '{:32b}'.format(val)
    if 32 != len(binary):
        raise Exception("strings not the same length: ", len(binary),  int(val))

    return val

def to_bin_twos(val):

    min, max = get_min_max()

    if val < min:
        val = val + 2**32

    if val > max:
        val = val - 2**32


    pos_bin = '{:032b}'.format(abs(val))

    truth = pos_bin
    if val < 0:
        flipped = "".join('1' if x == '0' else '0' for x in pos_bin)
        one = '{:032b}'.format(1)
        neg_bin = '{:032b}'.format(int(flipped, 2) + int(one, 2))
        truth = neg_bin

    if 32 != len(truth):
        raise Exception("strings not the same length: ", len(truth), ", ", int(truth))

    return truth

def get_column_names_Add32():
    return ["A[32]", "B[32]", "Cin[1]", "V[1]", "C[32]"]

def generate_random_samples_add32(num_samples):

    min, max = get_min_max()

    lst = []

    for i in range(0, num_samples):


        A = r.randint(min, max)
        B = r.randint(min, max)
        Cin = r.randint(0, 1)
        C = A + B + Cin
        V = 0


        if C > max or C < min:
            V = 1
            C = refit_to_32bit(C)

        print("A: ", str(A), "B: ", str(B), "C: ", str(C))

        Cin_print = str(Cin)
        V_print = str(V)

        lst.append([A, B, Cin_print, V_print, C])

    return lst



if __name__ == "__main__":
    print("runnign Add32 as main")