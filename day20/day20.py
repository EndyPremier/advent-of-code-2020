import os, re
from math import prod
from itertools import product

from utils import get_data, run


# INPUT SECTION
def get_input():
    DIR_ROOT = os.path.dirname(__file__)
    puzzle_input = get_data(DIR_ROOT)
    return puzzle_input


# HELPER FUNCTIONS
## TILE TRANSFORM
def transposed(tile):
    return tuple(''.join(row) for row in zip(*tile))

def reversed_tile(tile):
    return tuple(''.join(reversed(row)) for row in tile)

def rotations(tile):
    ans = [tile]
    for _ in range(3):
        ans.append(reversed_tile(transposed(ans[-1])))
    return ans

def group(tile):
    return rotations(tile) + rotations(transposed(tile))

## INPUT PROCESSSING
TILE_REGEX = r'Tile (\d+):\n(([.#]{10}\n?){10})'
def extract_tile(tile_input):
    match = re.match(TILE_REGEX, tile_input)
    tile_id, tile = int(match[1]), tuple(match[2].split())
    return tile_id, tile

def extract_input(puzzle_input):
    tiles = {}
    for tile_input in puzzle_input.split('\n\n'):
        tile_id, tile = extract_tile(tile_input)
        tiles[tile_id] = group(tile)
    return tiles

## SOLVING
def same_row_border(top, bot):
    return top[-1] == bot[0]

def same_col_border(left, right):
    return all(l[-1] == r[0] for l, r in zip(left, right))

def solve(tiles, grid=None, pos=0):
    if pos == 0:
        N = int(len(tiles) ** 0.5)
        tiles = tiles.copy()
        grid = [[None] * N for _ in range(N)]
    if len(tiles) == 0:
        return True
    N = len(grid)
    r, c = pos // N, pos % N
    keys = tuple(tiles.keys())
    for tile_id in keys:
        tile_group = tiles[tile_id]
        del tiles[tile_id]
        for tile in tile_group:
            if r and not same_row_border(grid[r-1][c][1], tile):
                continue
            if c and not same_col_border(grid[r][c-1][1], tile):
                continue
            grid[r][c] = (tile_id, tile)
            result = solve(tiles, grid, pos+1)
            if result:
                return grid if r == 0 and c == 0 else True
        tiles[tile_id] = tile_group

def get_solution():
    return solve(extract_input(get_input()))

## RECONSTRUCTION
def reconstruct(solution):
    N = len(solution)
    return [
        ''.join(tile_row[j][1][i][1:9] for j in range(N))
        for tile_row in solution for i in range(1, 9)
    ]

# GLOBAL VALUES
MONSTER = (
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
)


# MAIN FUNCTIONS
def part_one():
    solution = get_solution()
    return prod(
        solution[r][c][0]
        for r in range(-1, 1)
        for c in range(-1, 1)
    )

def part_two():
    solution = get_solution()
    board = reconstruct(solution)
    L = len(board)
    b_count = sum(row.count('#') for row in board)
    m_count = sum(row.count('#') for row in MONSTER)
    min_count = b_count
    for pattern in group(MONSTER):
        R, C = len(pattern), len(pattern[0])
        matches = 0
        for r, c in product(range(L - R + 1), range(L - C + 1)):
            matches += all(
                pattern[dr][dc] == ' ' or board[r+dr][c+dc] == '#'
                for dr, dc in product(range(R), range(C))
            )
        count = b_count - matches * m_count
        if count < min_count:
            min_count = count
    return min_count

# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
