import os, re

from utils import get_data, map_sum


# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
passports = [
    dict(entry.split(':') for entry in passport.split())
    for passport in get_data(DIR_ROOT).split('\n\n')
]


# GLOBAL VALUES
FIELD_REGEX = {
    'byr': r'(19[2-9]\d|200[0-2])',
    'iyr': r'20(1\d|20)',
    'eyr': r'20(2\d|30)',
    'hgt': r'(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)',
    'hcl': r'#[0-9a-f]{6}',
    'ecl': r'(amb|blu|brn|gry|grn|hzl|oth)',
    'pid': r'\d{9}',
}


# MAIN FUNCTIONS
def part_one():
    def validate(passport):
        passport_entries = set(passport.keys())
        required_entries = set(FIELD_REGEX.keys())
        return passport_entries.issuperset(required_entries)

    return map_sum(validate, passports)

def part_two():
    def validate(passport):
        try:
            for field, regex in FIELD_REGEX.items():
                assert re.fullmatch(regex, passport[field])
        except Exception as e:
            return False
        return True

    return map_sum(validate, passports)


# RUNNING FUNCTION
if __name__ == "__main__":
    print('Part 1:', part_one()) # 206
    print('Part 2:', part_two()) # 123
