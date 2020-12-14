"""DAY 06: Custom Customs

ORIGINAL LINK: https://adventofcode.com/2020/day/6

The puzzle input are in groups, separated by double line breaks with
individual people being a non-empty line with each characters are
questions that are answered 'yes'. Each person can be considered as a
set of elements where the 'yes' questions are such elements.

Part one per group asks for the total count of the Union of those sets
in the group. (e.g. 'ab' | 'ac' == 'abc')

Part two per group ask for the total count of the Intersect of those
sets in the group. (e.g. 'ab' & 'ac' == 'a' )
"""

import os

from utils import get_data, run, map_list


# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
groups = [
    map_list(set, group.split())
    for group in get_data(DIR_ROOT).split('\n\n')
]


# MAIN FUNCTIONS
def part_one():
    """TIME COMPLEXITY: O(N)
    where N is the number of all the characters in the input
    """
    return sum(len(set.union(*group)) for group in groups)

def part_two():
    """TIME COMPLEXITY: O(N)
    where N is the number of all the characters in the input
    """
    return sum(len(set.intersection(*group)) for group in groups)


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
