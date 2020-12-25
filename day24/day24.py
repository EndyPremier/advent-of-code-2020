import os, re
from collections import Counter

from utils import get_data, run


# INPUT SECTION
def get_input():
    DIR_ROOT = os.path.dirname(__file__)
    puzzle_input = get_data(DIR_ROOT)
    return puzzle_input.split()


# HELPER FUNCTIONS
DIRECTIONS = {
    'e': ( 1, 0), 'se': ( 0, -1), 'sw': (-1, -1),
    'w': (-1, 0), 'nw': ( 0,  1), 'ne': ( 1,  1),
}

DIRECTION_REGEX = r'[ns]?[ew]'
def parse_directions(directions):
    x = y = 0
    for direction in re.finditer(DIRECTION_REGEX, directions):
        dx, dy = DIRECTIONS[direction[0]]
        x, y = x + dx, y + dy
    return x, y

INPUT_POS = {
    k for k, v in Counter(map(parse_directions, get_input())).items() if v % 2
}


def get_neighbors(x, y):
    return { (x + dx, y + dy) for dx, dy in DIRECTIONS.values() }

def get_all_neighbors(tiles):
    return {
        neighbor
        for pos in tiles
        for neighbor in get_neighbors(*pos)
    }

def black_count(tiles, x, y):
    return len(get_neighbors(x, y) & tiles)

def next_black(tiles, pos):
    count = black_count(tiles, *pos)
    return count in range(1, 3) if pos in tiles else count == 2

def next_grid(tiles):
    return {
        pos for pos in get_all_neighbors(tiles)
        if next_black(tiles, pos)
    }


# MAIN FUNCTIONS
def part_one():
    return len(INPUT_POS)

def part_two():
    curr = INPUT_POS.copy()
    for i in range(1, 101):
        curr = next_grid(curr)
    return len(curr)


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
