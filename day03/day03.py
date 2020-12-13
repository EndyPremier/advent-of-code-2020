import os
from itertools import count
from math import prod

from utils import get_data, map_list


# INPUT HELPER FUNCTIONS
is_tree = lambda c: c == '#'
tree_line = lambda line: map_list(is_tree, line)


# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
tree_map = map_list(tree_line, get_data(DIR_ROOT).split())


# HELPER FUNCTIONS
def trees_hit(right, down):
    return sum(
        row[col % len(row)] for row, col
        in zip(tree_map[down::down], count(right, right))
    )


# MAIN FUNCTIONS
def part_one():
    return trees_hit(3, 1)

def part_two():
    args = [(1,1), (3,1), (5,1), (7,1), (1,2)]    # noqa: E231
    return prod(trees_hit(*arg) for arg in args)


# RUNNING FUNCTION
if __name__ == "__main__":
    print('Part 1:', part_one())
    print('Part 2:', part_two())
