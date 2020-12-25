import os

from utils import get_data, run


# INPUT SECTION
def get_input():
    DIR_ROOT = os.path.dirname(__file__)
    puzzle_input = get_data(DIR_ROOT)
    return map(int, puzzle_input.split())


# GLOBAL VALUES
MOD = 20201227

# HELPER FUNCTIONS
def transform(pow, base=7, mod=MOD):
    if pow == 0:
        return 1
    if pow % 2:
        return (transform(pow - 1, base, mod) * base) % mod
    else:
        return (transform(pow // 2, base, mod) ** 2) % mod


# MAIN FUNCTIONS
def part_one():
    val = 1
    keys = set(get_input())
    for i in range(MOD):
        if val in keys:
            break
        val = (val * 7) % MOD
    other = (keys ^ { val }).pop()
    return transform(i, other)

def part_two():
    pass


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
