from Add32 import generate_random_samples_add32, get_column_names_Add32
import pandas as pd
import numpy as np
from FileOutputter import output_file
from LeftShift32 import generate_random_examples_shift32, get_col_names_shift32

from ALUGenerators import add_subtract_test_generator, get_add_ALU_test_col_names, shift_test_generator, bitwise_logic_generator, bitwise_comparison_generator


if __name__ == '__main__':

    row_names = get_add_ALU_test_col_names()
    generated = bitwise_comparison_generator(1000)

    output_file(row_names, generated, filename="bitwise_comp.txt")

