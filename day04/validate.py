import re

FIELD_REGEX = {
    'byr': r'(19[2-9]\d|200[0-2])',
    'iyr': r'20(1\d|20)',
    'eyr': r'20(2\d|30)',
    'hgt': r'(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)',
    'hcl': r'#[0-9a-f]{6}',
    'ecl': r'(amb|blu|brn|gry|grn|hzl|oth)',
    'pid': r'\d{9}',
}

def validate_part_one(passport):
    passport_entries = set(passport.keys())
    required_entries = set(FIELD_REGEX.keys())
    return passport_entries.issuperset(required_entries)

def validate_part_two(passport):
    try:
        for field, regex in FIELD_REGEX.items():
            assert re.fullmatch(regex, passport[field])
    except Exception as e:
        return False
    return True
