import os
from itertools import chain, combinations

from utils import get_data, run


# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
puzzle_input = get_data(DIR_ROOT).split('\n')


# HELPER FUNCTIONS
def get_X_bits(val):
    return [2 ** i for i, c in enumerate(reversed(val)) if c == 'X']

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


# MAIN FUNCTIONS
def part_one():
    mask_zero = 2**36 - 1
    mask_one  = 0
    memory    = {}
    for line in puzzle_input:
        register, value = line.split(' = ')
        if register == 'mask':
            mask_zero = int(value.replace('X', '1'), 2)
            mask_one  = int(value.replace('X', '0'), 2)
        else:
            address = int(register[4:-1])
            value   = int(value) & mask_zero | mask_one
            memory[address] = value
    return sum(val for val in memory.values())

def part_two():
    mask_one  = 0
    mask_zero = 0
    float_bit = []
    memory    = {}
    for line in puzzle_input:
        register, value = line.split(' = ')
        if register == 'mask':
            mask_one  = int(value.replace('X', '1'), 2)
            mask_zero = int(value.replace('0', '1').replace('X', '0'), 2)
            float_bit = get_X_bits(value)
        else:
            root_address = int(register[4:-1])
            root_address = (root_address | mask_one) & mask_zero
            value = int(value)
            for bits in powerset(float_bit):
                float_val = sum(bits)
                address   = root_address + float_val
                memory[address] = value
    return sum(val for val in memory.values())


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
