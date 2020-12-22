import os, re
from collections import Counter, defaultdict
from math import prod

from utils import get_data, run


# INPUT SECTION
def get_input():
    DIR_ROOT = os.path.dirname(__file__)
    puzzle_input = get_data(DIR_ROOT)
    return puzzle_input


# HELPER FUNCTIONS
## INPUT PROCESSSING
def process_tile_borders(tile):
    yield ''.join(sorted((tile[:10], tile[:10][::-1])))      # up
    yield ''.join(sorted((tile[9::11], tile[9::11][::-1])))  # right
    yield ''.join(sorted((tile[-10:][::-1], tile[-10:])))    # dowm
    yield ''.join(sorted((tile[::11][::-1], tile[::11])))    # left

TILE_REGEX = r'Tile (\d+):\n(([.#]{10}\n?){10})'
def extract_tile(tile_input):
    match = re.match(TILE_REGEX, tile_input)
    tile_id, tile = int(match[1]), match[2]
    return tile_id, tile

def extract_input(puzzle_input):
    tiles = {}
    for tile_input in puzzle_input.split('\n\n'):
        tile_id, tile = extract_tile(tile_input)
        tiles[tile_id] = tile
    return tiles

## PROCESS
def get_border_group(tiles):
    return {
        tile_id: list(process_tile_borders(tile))
        for tile_id, tile in tiles.items()
    }

def get_border_count(border_group):
    border_count = defaultdict(set)
    for tile_id, borders in border_group.items():
        for border in borders:
            border_count[border].add(tile_id)
    return border_count

def is_corner(borders, border_count):
    edge_count = sum(len(border_count[border]) == 1 for border in borders)
    return edge_count == 2

def get_corners(border_group, border_count):
    return (
        tile_id
        for tile_id, borders in border_group.items()
        if is_corner(borders, border_count)
    )

def get_first_corner(border_group, border_count):
    for tile_id, borders in border_group.items():
        if is_corner(borders, border_count):
            return tile_id

# GLOBAL VALUES



# MAIN FUNCTIONS
def part_one():
    tiles = extract_input(get_input())
    border_group = get_border_group(tiles)
    border_count = get_border_count(border_group)
    corners = get_corners(border_group, border_count)
    return prod(corners)

def part_two():
    tiles = extract_input(get_input())
    border_group = get_border_group(tiles)
    border_count = get_border_count(border_group)


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
