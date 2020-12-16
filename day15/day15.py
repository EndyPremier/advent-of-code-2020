import os

from utils import get_data, run, map_list


# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
puzzle_input = map_list(int, get_data(DIR_ROOT).split(','))


# HELPER FUNCTIONS
def run_game(to_step):
    memo = { num: i for i, num in enumerate(puzzle_input[:-1], start=1) }
    prev = puzzle_input[-1]
    for turn in range(len(puzzle_input), to_step):
        if prev in memo:
            diff = turn - memo[prev]
            memo[prev] = turn
            prev = diff
        else:
            memo[prev] = turn
            prev = 0
    return prev


# MAIN FUNCTIONS
def part_one():
    return run_game(2020)

def part_two():
    return run_game(30000000)


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
