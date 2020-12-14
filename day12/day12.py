import os

from utils import get_data, run


# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
puzzle_input = get_data(DIR_ROOT).split()


# MAIN FUNCTIONS
def part_one():
    x = y = 0
    direction = 0
    for instruction in puzzle_input:
        action = instruction[:1]
        value  = int(instruction[1:])
        if action in 'EW':
            x += (1 if action == 'E' else -1) * value
        if action in 'NS':
            y += (1 if action == 'N' else -1) * value
        if action in 'LR':
            value //= 90
            value *= -1 if action == 'L' else 1
            direction = (direction + value) % 4
        if action == 'F':
            if direction % 2:  # in 'SN'
                y += value * (direction - 2)
            else:              # in 'EW'
                x -= value * (direction - 1)
    return abs(x) + abs(y)

def part_two():
    pos_x, pos_y = 0, 0
    way_x, way_y = 10, 1
    for instruction in puzzle_input:
        action = instruction[:1]
        value  = int(instruction[1:])
        if action in 'EW':
            way_x += (1 if action == 'E' else -1) * value
        if action in 'NS':
            way_y += (1 if action == 'N' else -1) * value
        if action in 'LR':
            value = value // 90
            value *= -1 if action == 'L' else 1
            value %= 4
            if value == 1:
                way_x, way_y = way_y, -way_x
            if value == 2:
                way_x, way_y = -way_x, -way_y
            if value == 3:
                way_x, way_y = -way_y, way_x
        if action == 'F':
            pos_x += way_x * value
            pos_y += way_y * value
    return abs(pos_x) + abs(pos_y)


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
