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

from utils import get_data
import os


# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
input_text = get_data(DIR_ROOT)


# MAIN FUNCTIONS
def part_one():
    """TIME COMPLEXITY: O(N)
    where N is the number of all the characters in the input
    """
    return sum(
        len(set.union(*(map(set, group.split()))))
        for group in input_text.split('\n\n')
    )

def part_two():
    """TIME COMPLEXITY: O(N)
    where N is the number of all the characters in the input
    """
    return sum(
        len(set.intersection(*(map(set, group.split()))))
        for group in input_text.split('\n\n')
    )


# RUNNING FUNCTION
if __name__ == "__main__":
    print('Part 1:', part_one()) # 6630
    print('Part 2:', part_two()) # 3437
