from functools import reduce


with open('input.txt', 'r') as in_file:
    passes = in_file.read().split('\n')


def col_id(board_pass):
    ret = 0
    for c in board_pass:
        ret = ret * 2 + (c in 'BR')
    return ret


def part_one(passes=passes):
    return max(map(col_id, passes))

def part_two(passes=passes):
    sum_series = lambda x: x * (x + 1) // 2
    sum_range = lambda a, b: sum_series(b - 1) - sum_series(a)

    min_id, max_id = None, None
    curr_sum = 0
    for id in map(col_id, passes):
        if min_id is None:
            min_id = max_id = id
        elif id < min_id:
            curr_sum += sum_range(id, min_id)
            min_id = id
        elif max_id < id:
            curr_sum += sum_range(max_id, id)
            max_id = id
        else:
            curr_sum -= id
    return curr_sum


print('Part 1:', part_one())
print('Part 2:', part_two())