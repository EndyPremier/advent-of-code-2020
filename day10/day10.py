import os
from collections import defaultdict

from utils import get_data, map_sort


# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
puzzle_input = map_sort(int, get_data(DIR_ROOT).split())


# MAIN FUNCTIONS
def part_one():
    ones = puzzle_input[0] == 1
    threes = 2 if puzzle_input[0] == 3 else 1
    for a, b in zip(puzzle_input[:-1], puzzle_input[1:]):
        if b - a == 1:
            ones += 1
        elif b - a == 3:
            threes += 1
    return ones * threes

def part_two():
    permutations = defaultdict(lambda: 0)
    permutations[0] = 1
    for n in puzzle_input:
        permutations[n] = sum(permutations[m] for m in range(n-3, n))
    return permutations[puzzle_input[-1]]


# RUNNING FUNCTION
if __name__ == "__main__":
    print('Part 1:', part_one())
    print('Part 2:', part_two())
