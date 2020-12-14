import os

from utils import get_data, run


# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
puzzle_input = get_data(DIR_ROOT).split()


# HELPER FUNCTIONS
def add_neighbor(neighbors, prev_pos, next_pos):
    if prev_pos is not None:
        dist = max(abs(a - b) for a, b in zip(prev_pos, next_pos))
        neighbors[next_pos][prev_pos] = dist
        neighbors[prev_pos][next_pos] = dist

def make_graph(puzzle_input):
    rows, cols = len(puzzle_input), len(puzzle_input[0])
    diags = rows + cols - 1

    prev_cols = [None] * cols
    prev_for_diags = [None] * diags
    prev_bac_diags = [None] * diags
    neighbors = {}
    for r, row in enumerate(puzzle_input):
        prev_row = None
        for c, seat in enumerate(row):
            if seat != 'L':
                continue
            curr_pos = (r, c)
            neighbors[curr_pos] = {}
            # row
            add_neighbor(neighbors, prev_row, curr_pos)
            prev_row = curr_pos
            # column
            add_neighbor(neighbors, prev_cols[c], curr_pos)
            prev_cols[c] = curr_pos
            # forward diagonal
            add_neighbor(neighbors, prev_for_diags[r+c], curr_pos)
            prev_for_diags[r+c] = curr_pos
            # back diagonal
            add_neighbor(neighbors, prev_bac_diags[r-c], curr_pos)
            prev_bac_diags[r-c] = curr_pos

    return neighbors

def run_program(part):
    seats = { pos: False for pos in neighbors }
    while True:
        # get positions to change
        to_change = []
        for curr_pos, curr_neighbors in neighbors.items():
            # count occcupied neighbors
            occupied = sum(
                seats[neighbor] and (dist == 1 or part == 2)
                for neighbor, dist in curr_neighbors.items()
            )
            # check conditions
            required = 4 if part == 1 else 5
            if seats[curr_pos] and occupied >= required:
                to_change.append(curr_pos)
            elif not seats[curr_pos] and occupied == 0:
                to_change.append(curr_pos)
        # check if there is things to change
        if not to_change:
            break
        for pos in to_change:
            seats[pos] = not seats[pos]
    return sum(seats.values())


# GLOBAL VALUES
rows, cols = len(puzzle_input), len(puzzle_input[0])
neighbors = make_graph(puzzle_input)


# MAIN FUNCTIONS
def part_one():
    return run_program(part=1)

def part_two():
    return run_program(part=2)


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
