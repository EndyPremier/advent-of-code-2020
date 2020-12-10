import os
from collections import Counter

from utils import get_data, map_list


# INPUT HELPERS


# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
puzzle_input = map_list(int, get_data(DIR_ROOT).split())


# GLOBAL VALUES


# HELPER FUNCTIONS



# MAIN FUNCTIONS
def part_one():
    memo = Counter(
        (a + b)
        for i, a in enumerate(puzzle_input[:25], start=1)
        for b in puzzle_input[i:25]
    )
    for i, a in enumerate(puzzle_input[25:]):
        if a not in memo:
            return a
        for b in puzzle_input[i+1:i+25]:
            memo[puzzle_input[i] + b] -= 1
            memo[a + b] += 1

def part_two():
    to_find = part_one()
    curr_sum = 0
    l = r = 0
    while curr_sum != to_find:
        if curr_sum < to_find:
            curr_sum += puzzle_input[r]
            r += 1
        else:
            curr_sum -= puzzle_input[l]
            l += 1
    return min(puzzle_input[l:r]) + max(puzzle_input[l:r])


# RUNNING FUNCTION
if __name__ == "__main__":
    print('Part 1:', part_one()) # expected answer
    print('Part 2:', part_two()) # expected answer
