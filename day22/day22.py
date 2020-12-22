import os

from utils import get_data, run, map_tuple


# INPUT SECTION
def get_input():
    DIR_ROOT = os.path.dirname(__file__)
    puzzle_input = get_data(DIR_ROOT)
    return puzzle_input

def get_cards(puzzle_input=get_input()):
    return (
        map_tuple(int, deck.split('\n')[1:])
        for deck in puzzle_input.split('\n\n')
    )


# HELPER FUNCTIONS
def get_total(group):
    return sum(i * c for i, c in enumerate(group[::-1], 1))

def game(recurse=False, sub_game=False, p1=None, p2=None):
    if not sub_game:
        p1, p2 = get_cards()
    memo = set()
    while p1 and p2:
        prev_state = (p1, p2)
        if prev_state in memo:
            return bool(p1) if sub_game else get_total(p1)
        else:
            memo.add(prev_state)
        c1, p1 = p1[0], p1[1:]
        c2, p2 = p2[0], p2[1:]
        if recurse and c1 <= len(p1) and c2 <= len(p2):
            c1_win = game(True, True, p1[:c1], p2[:c2])
        else:
            c1_win = c1 > c2
        if c1_win:
            p1 += (c1, c2)
        else:
            p2 += (c2, c1)
    return bool(p1) if sub_game else get_total(p1 + p2)


# MAIN FUNCTIONS
def part_one():
    return game(recurse=False)

def part_two():
    return game(recurse=True)


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
