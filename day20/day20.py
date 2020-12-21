import os, re
from collections import defaultdict
from math import prod, sqrt

from utils import get_data, run, map_sum


# INPUT SECTION
def get_input():
    DIR_ROOT = os.path.dirname(__file__)
    puzzle_input = get_data(DIR_ROOT)
    return puzzle_input


# HELPER FUNCTIONS
## INPUT PROCESSSING
def process_tile_borders(tile):
    return {
        'nU': tile[:10],          # normal  up
        'nR': tile[9::11],        # normal  right
        'nD': tile[-10:][::-1],   # normal  dowm
        'nL': tile[::11][::-1],   # normal  left
        'fL': tile[::11],         # flipped left
        'fD': tile[-10:],         # flipped down
        'fR': tile[9::11][::-1],  # flipped right
        'fU': tile[:10][::-1],    # flipped up
    }

TILE_REGEX = r'Tile (\d+):\n(([.#]{10}\n?){10})'
def extract_tile(tile_input):
    match = re.match(TILE_REGEX, tile_input)
    tile_id, tile = int(match[1]), match[2]
    return tile_id, tile

def extract_input(puzzle_input):
    tiles = {}
    borders = {}
    for tile_input in puzzle_input.split('\n\n'):
        tile_id, tile = extract_tile(tile_input)
        tile_borders = process_tile_borders(tile)
        tiles[tile_id] = tile
        borders[tile_id] = tile_borders
    return tiles, borders

## BORDER CONNECTION
def connect_borders(tiles):
    def defaultdict_section():
        def empty_tuple():
            return (None, None)
        return defaultdict(empty_tuple)
    border_count = defaultdict(lambda: 0)
    section_to_border = {}
    border_to_borders = defaultdict(defaultdict_section)
    for tile_a, tile in tiles.items():
        for region_a, section in tile.items():
            border_count[section] += 1
            section = section[::-1]
            border_count[section] += 1
            if section in section_to_border:
                tile_b, region_b = section_to_border[section]
                border_to_borders[tile_a][region_a] = (tile_b, region_b)
                border_to_borders[tile_b][region_b] = (tile_a, region_a)
            else:
                section_to_border[section] = (tile_a, region_a)
    print(border_count)
    return border_to_borders

def is_corner(border: dict):
    return map_sum(lambda n: n != (None, None), border.values()) == 4

# GLOBAL VALUES
puzzle_input = get_input()
tiles, borders = extract_input(puzzle_input)
connections = connect_borders(borders)

"""
assertion:
- all connection between tiles are unique
- corner have 4 filled entries,
- edges have 6 filled entries,
- and center patch has 8 filled entires.
- just check if the tile are just corners
"""


# MAIN FUNCTIONS
def part_one():
    return prod(
        tile_id
        for tile_id, tile in connections.items()
        if is_corner(tile)
    )

def part_two():
    return -1


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
