from data import DATA
from validate import validate_part_one, validate_part_two

def count_valid(validator, iterable):
    return sum(map(validator, iterable))

print("Part 1:", count_valid(validate_part_one, DATA))
print("Part 2:", count_valid(validate_part_two, DATA))
