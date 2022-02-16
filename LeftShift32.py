import random as r

def get_col_names_shift32():
    return ["B[32]", "Sa[5]", "Cin[1]", "C[32]"]

def generate_random_examples_shift32(num_samples):

    formats_32 = ['{:032b}', '{:d}', '{:#x}']
    formats_5 = ['{:05b}', '{:d}', '{:#x}']
    lst = []

    for i in range(0, num_samples):
        B = r.choice([r.randint(0, 2**32 - 1)])
        B_calc = '{:032b}'.format(B)
        Sa = r.randint(0, 2**5 - 1)
        Cin = r.randint(0, 1)
        C = B_calc[Sa:] + str(Cin)*Sa
        C = int(C, 2)

        B_print = r.choice(formats_32).format(B)
        C_print = r.choice(formats_32).format(C)
        Sa_print = r.choice(formats_5).format(Sa)
        Cin_print = str(Cin)

        lst.append([B_print, Sa_print, Cin_print, C_print])

    return lst



if __name__ == "__main__":
    print("runnign LeftShift32 as main")