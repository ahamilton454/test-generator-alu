from enum import Enum
import random as r
from Add32 import get_min_max,  refit_to_32bit, to_bin_twos

class ShiftEnums(Enum):
    SHIFT_LEFT = 1
    SHIFT_RIGHT = 2
    SHIFT_RIGHT_ARTH = 3

class Operation(Enum):
    ADD = 1
    SUBTRACT = 2

def rand_32bit():
    return r.randint((-2 ** 32)/2 + 1, (2 ** 32)/2 - 1)

def shift_test_generator(num_tests):

    lst = []
    for _ in range(0, num_tests):
        shift_type = r.choice([ShiftEnums.SHIFT_LEFT, ShiftEnums.SHIFT_RIGHT, ShiftEnums.SHIFT_RIGHT_ARTH])


        B = to_bin_twos(rand_32bit())
        C = B
        Sa = r.randint(0, 31)

        if shift_type == ShiftEnums.SHIFT_LEFT:
            C = C[Sa:] + "0" * Sa
            Op = r.choice(["1101", "1100"])
        elif shift_type == ShiftEnums.SHIFT_RIGHT:
            C = ("0" * abs(Sa)) + C[: -Sa if Sa != 0 else 32]
            print(Sa, " ", len(C))
            Op = r.choice(["0000"])
        elif shift_type == ShiftEnums.SHIFT_RIGHT_ARTH:
            C = (C[0] * abs(Sa)) + C[: -Sa if Sa != 0 else 32]
            Op = r.choice(["0001"])

        if 32 != len(C):
            raise Exception("strings not the same length: ", shift_type,  len(C))

        lst.append([rand_32bit(), B, '{:05b}'.format(Sa), Op, str(0), C])

    return lst

def get_add_ALU_test_col_names():
    return ["A[32]", "B[32]", "Sa[5]", "Op[4]", "V[1]", "C[32]"]

def add_subtract_test_generator(num_tests):

    min, max = get_min_max()
    lst = []

    for _ in range(0, num_tests):
        operation_type = r.choice([Operation.ADD, Operation.SUBTRACT])

        A = rand_32bit()
        B = rand_32bit()
        Sa = r.randint(0, 31)
        V = 0

        if operation_type == Operation.ADD:
            C = A + B
            Op = r.choice(["1010", "1011"])
        elif operation_type == Operation.SUBTRACT:
            C = A - B
            Op = r.choice(["1110", "1111"])

        if C > max or C < min:
            C = refit_to_32bit(C)
            V = 1

        Sa = '{:05b}'.format(Sa)
        V = str(V)



        lst.append([A, B, Sa, Op, V, C])

    return lst


class BitwiseLogic(Enum):
    AND = 1
    OR = 2
    XOR = 3
    XNOR = 4

def bitwise_logic_generator(num_tests):

    lst = []

    for _ in range(0, num_tests):
        operation_type = r.choice([BitwiseLogic.AND, BitwiseLogic.OR, BitwiseLogic.XOR, BitwiseLogic.XNOR])

        A = rand_32bit()
        B = rand_32bit()
        Sa = r.randint(0, 31)
        V = 0

        if operation_type == BitwiseLogic.AND:
            C = A & B
            Op = "1001"
        elif operation_type == BitwiseLogic.OR:
            C = A | B
            Op = "1000"
        elif operation_type == BitwiseLogic.XOR:
            C = A ^ B
            Op = "0110"
        elif operation_type == BitwiseLogic.XNOR:
            C = ~ (A | B)
            Op = "0111"

        Sa = '{:05b}'.format(Sa)
        V = str(V)



        lst.append([A, B, Sa, Op, V, C])

    return lst


class BitwiseComp(Enum):
    NE = 1
    EQ = 2
    LE = 3
    GT = 4

def bitwise_comparison_generator(num_tests):


    lst = []

    for _ in range(0, num_tests):

        operation_type = r.choice([BitwiseComp.NE, BitwiseComp.EQ, BitwiseComp.LE, BitwiseComp.GT])

        A = rand_32bit()
        B = r.choice([rand_32bit(), rand_32bit(), rand_32bit(), A])
        Sa = r.randint(0, 31)
        V = 0

        if operation_type == BitwiseComp.NE:
            Op = "0100"
            if A != B:
                C = 1
            else:
                C = 0
        elif operation_type == BitwiseComp.EQ:
            Op = "0101"
            if A == B:
                C = 1
            else:
                C = 0
        elif operation_type == BitwiseComp.LE:
            Op = "0010"
            if B <= 0:
                C = 1
            else:
                C = 0
        elif operation_type == BitwiseComp.GT:
            Op = "0011"
            if B > 0:
                C = 1
            else:
                C = 0



        Sa = '{:05b}'.format(Sa)
        V = str(V)



        lst.append([A, B, Sa, Op, V, C])

    return lst
