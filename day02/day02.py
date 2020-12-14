import os, re

from utils import get_data, run, map_list, map_sum


# INPUT HELPER FUNCTIONS
REGEX = r'(\d+)-(\d+) (\w): (\w+)'
def parse_password_policy(line):
    match = re.match(REGEX, line)
    return int(match[1]), int(match[2]), match[3], match[4]


# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
password_list = map_list(parse_password_policy, get_data(DIR_ROOT).split('\n'))


# HELPER FUNCTIONS
def valid_count(policy):
    return map_sum(lambda args: policy(*args), password_list)


# MAIN FUNCTIONS
def part_one():
    def policy(min_count, max_count, letter, password):
        return password.count(letter) in range(min_count, max_count + 1)
    return valid_count(policy)

def part_two():
    def policy(i, j, letter, password):
        return (password[i-1] == letter) != (password[j-1] == letter)
    return valid_count(policy)


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
