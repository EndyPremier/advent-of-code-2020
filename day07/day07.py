import os, re
from collections import defaultdict

from utils import get_data, map_dict, map_sum


# INPUT HELPERS
BAG_WHOLE_REGEX = re.compile(r'([a-z]+ [a-z]+) bags contain (.+)\.')
def bag_regex(line):
    bag, contain_list = BAG_WHOLE_REGEX.match(line).groups()
    contains = {}
    for bag_type in contain_list.split(', '):
        if bag_type == 'no other bags':
            continue
        count, adj, color, _ = bag_type.split()
        contains[f'{adj} {color}'] = int(count)
    return bag, contains

# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
bag_list = map_dict(bag_regex, get_data(DIR_ROOT).split('\n'))


# MAIN FUNCTIONS
def part_one():
    is_in = defaultdict(set)
    for parent_bag, contains in bag_list.items():
        for child_bag in contains:
            is_in[child_bag].add(parent_bag)

    has_checked = is_in['shiny gold'].copy()
    to_check = is_in['shiny gold'].copy()
    while to_check:
        bag_check = to_check.pop()
        for parent_bag in is_in[bag_check]:
            if parent_bag not in has_checked:
                has_checked.add(parent_bag)
                to_check.add(parent_bag)

    return len(has_checked)

def part_two():
    def get_bag_required_count(bag, memo={}):
        if len(bag_list[bag]) == 0:
            return 0
        memo[bag] = sum(
            count * (get_bag_required_count(child_bag) + 1)
            for child_bag, count in bag_list[bag].items()
        )
        return memo[bag]

    return get_bag_required_count('shiny gold')


# RUNNING FUNCTION
if __name__ == "__main__":
    print('Part 1:', part_one())
    print('Part 2:', part_two())
