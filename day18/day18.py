import os, re
from operator import add, mul
from math import prod

from utils import get_data, run, mapf, map_sum


# INPUT HELPERS


# INPUT SECTION
def get_input():
    DIR_ROOT = os.path.dirname(__file__)
    puzzle_input = get_data(DIR_ROOT).split('\n')
    return puzzle_input


# HELPER FUNCTIONS
TOKEN_REGEX = r"([()+*]|\d+)"
def tokenize(string_input):
    return re.findall(TOKEN_REGEX, string_input)

def eval_eq_1(string_input):
    tokens = tokenize(string_input)
    stack = []
    curr_val, curr_op = 0, add
    for token in tokens:
        if token == '(':
            stack.append((curr_val, curr_op))
            curr_val, curr_op = 0, add
        elif token == ')':
            old_val, old_op = stack.pop()
            curr_val = old_op(old_val, curr_val)
        elif token == '+':
            curr_op = add
        elif token == '*':
            curr_op = mul
        else:
            curr_val = curr_op(curr_val, int(token))
    return curr_val

def eval_eq_2(string_input):
    if isinstance(string_input, str):
        tokens = tokenize(string_input)
    else:
        tokens = string_input

    paren_group = []
    l_parens = l_paren_index = 0
    for i, token in enumerate(tokens):
        if token == '(':
            if l_parens == 0:
                l_paren_index = i
            l_parens += 1
        elif token == ')':
            l_parens -= 1
            if l_parens == 0:
                paren_group.append((l_paren_index, i+1))

    while paren_group:
        l, r = paren_group.pop()
        tokens[l:r] = [eval_eq_2(tokens[l+1:r-1])]

    plus_indexes = [i for i, t in enumerate(tokens) if t == '+']
    while plus_indexes:
        mid = plus_indexes.pop()
        l = int(tokens[mid - 1])
        r = int(tokens[mid + 1])
        tokens[mid-1:mid+2] = [l + r]

    return mapf(prod)(int, tokens[::2])


# GLOBAL VALUES



# MAIN FUNCTIONS
def part_one():
    return map_sum(eval_eq_1, get_input())

def part_two():
    return map_sum(eval_eq_2, get_input())


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
