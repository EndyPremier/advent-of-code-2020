"""DAY 05: Binary Boarding

ORIGINAL LINK: https://adventofcode.com/2020/day/5

The puzzle defined the ticket as a 10 character representation of a
binary space partition (BSP), which the first 7 characters are either
'F' or 'B' and the last 3 being 'L' or 'R'.

Part one ask for the max value to be an integer representation, so the
string can be reinterpreted as binary where 'F' or 'L' is 0 and 'B' and
'R' is 1. Considering there is only 10 characters, the size of possible
values can only go up to 1024 (2^10).

Part two ask for the exact seat ID of the missing seat, and considering
that it's packed (should be a constant line of passengers), there's only
868 of 1024 filled, and the front and back shouldn't exist, it should
infer that somewhere in the boundary is unfilled. My approach has it sum
the min and max range (inclusive), and subtracted all of the IDs of the
filled seats. The naive way to get the sum of a range of numbers is just
add all of it, leading to O(N). Optimally, one can use a single formula
sum(range(N)) = N * (N+1) / 2 to get the same value in O(1), and getting
the sum for specific range A to B inclusive can be done with
sum_range(B) - sum_range(A-1), still being O(1).
"""

import os

from utils import get_data


# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
passes = get_data(DIR_ROOT).split()


# HELPER FUNCTIONS
def col_id(board_pass):
    ret = 0
    for c in board_pass:
        ret = ret * 2 + (c in 'BR')
    return ret


# GLOBAL VALUES
min_id = max_id = None
sum_id = 0
for id in map(col_id, passes):
    min_id = id if min_id is None or id < min_id else min_id
    max_id = id if max_id is None or max_id < id else max_id
    sum_id += id


# MAIN FUNCTIONS
def part_one():
    """TIME COMPLEXITY: O(N)
    where N is the number of all the lines in the input
    """
    return max_id

def part_two():
    """TIME COMPLEXITY: O(N)
    where N is the number of all the lines in the input
    """
    sum_series = lambda x: x * (x + 1) // 2                     # O(1)
    sum_range = lambda a, b: sum_series(b) - sum_series(a - 1)  # O(1)

    return sum_range(min_id, max_id) - sum_id


# RUNNING FUNCTION
if __name__ == "__main__":
    print('Part 1:', part_one())
    print('Part 2:', part_two())
