import re

REGEX = r'(\d+)-(\d+) (\w): (\w+)'
def parse_password_policy(line):
    match = re.match(REGEX, line)
    return int(match[1]), int(match[2]), match[3], match[4]

with open('input.txt', 'r') as file:
    password_list = list(map(parse_password_policy, file))


def part_one(min_count, max_count, letter, password):
    return password.count(letter) in range(min_count, max_count + 1)

def part_two(i, j, letter, password):
    return (password[i-1] == letter) != (password[j-1] == letter)

def valid_count(policy):
    return sum(map(lambda args: policy(*args), password_list))


print("Part 1:", valid_count(part_one))
print("Part 2:", valid_count(part_two))
