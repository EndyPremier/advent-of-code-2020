import os
from itertools import product

from utils import get_data, run


# INPUT SECTION
def get_input(dim):
    DIR_ROOT = os.path.dirname(__file__)
    puzzle_input = get_data(DIR_ROOT).split()
    init_active = {
        (x, y, *([0] * (dim - 2)))
        for y, row in enumerate(puzzle_input)
        for x, cube in enumerate(row)
        if cube == '#'
    }
    return init_active


# HELPER FUNCTIONS
def get_neighbors(old_pos):
    ranges = (range(i-1, i+2) for i in old_pos)
    points = product(*ranges)
    return {
        new_pos
        for new_pos in points
        if old_pos != new_pos
    }

def get_all_neighbors(active):
    return {
        pos
        for prev in active
        for pos in get_neighbors(prev)
        if pos not in active
    }

def neighbor_count(active, pos):
    intersect = active & get_neighbors(pos)
    return len(intersect)

def get_next_step(active):
    keep_active = {
        pos
        for pos in active
        if neighbor_count(active, pos) in range(2, 4)
    }
    become_active = {
        pos
        for pos in get_all_neighbors(active)
        if neighbor_count(active, pos) == 3
    }
    return become_active | keep_active

def run_six_cycle(dim):
    active = get_input(dim)
    for _ in range(6):
        active = get_next_step(active)
    return len(active)


# MAIN FUNCTIONS
def part_one():
    return run_six_cycle(dim=3)

def part_two():
    return run_six_cycle(dim=4)


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
