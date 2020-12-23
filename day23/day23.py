import os
from itertools import chain

from utils import get_data, run, map_tuple


# INPUT HELPERS


# INPUT SECTION
def get_input():
    DIR_ROOT = os.path.dirname(__file__)
    puzzle_input = get_data(DIR_ROOT)
    return map_tuple(int, puzzle_input)


# GLOBAL VALUES


# HELPER FUNCTIONS+
def connect(nexts, prevs, a, b):
    nexts[a], prevs[b] = b, a

def create_cycle(iterable, count):
    nexts = [0] * count
    prevs = [0] * count
    first = prev = None
    for n in iterable:
        if first is None:
            first = n
        if prev is not None:
            connect(nexts, prevs, prev, n)
        prev = n
    connect(nexts, prevs, prev, first)
    return nexts, prevs

def get_pickups(nexts, start_cup):
    ret = [nexts[start_cup]]
    ret.append(nexts[ret[-1]])
    ret.append(nexts[ret[-1]])
    return ret

def decrement(curr, l):
    return ((curr - 2) % l) + 1

def get_next(nexts, prevs, start_cup):
    l = len(nexts) - 1
    pickups = get_pickups(nexts, start_cup)
    to_find = decrement(start_cup, l)
    while to_find in pickups:
        to_find = decrement(to_find, l)
    new_start  = nexts[pickups[-1]]
    after_find = nexts[to_find]
    connect(nexts, prevs, start_cup, new_start)
    connect(nexts, prevs, to_find, pickups[0])
    connect(nexts, prevs, pickups[-1], after_find)
    return new_start

def encode_answer(nexts):
    num = nexts[1]
    ret = []
    while num != 1:
        ret.append(str(num))
        num = nexts[num]
    return ''.join(ret)


# MAIN FUNCTIONS
def part_one():
    init_cups = get_input()
    start_cup = init_cups[0]
    nexts, prevs = create_cycle(init_cups, 10)
    for _ in range(100):
        start_cup = get_next(nexts, prevs, start_cup)
    return encode_answer(nexts)

def part_two():
    MAX_CUPS   = 10 ** 6  #  1 million
    TURN_COUNT = 10 ** 7  # 10 million
    init_cups = get_input()
    start_cup = init_cups[0]
    other_cups = range(len(init_cups) + 1, MAX_CUPS + 1)
    nexts, prevs = create_cycle(chain(init_cups, other_cups), MAX_CUPS + 1)
    for i in range(TURN_COUNT):
        start_cup = get_next(nexts, prevs, start_cup)
    cup_a = nexts[1]
    cup_b = nexts[cup_a]
    return cup_a * cup_b


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
