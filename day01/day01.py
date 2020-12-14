import os

from utils import get_data, run, map_list


# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
puzzle_input = map_list(int, get_data(DIR_ROOT).split())


# GLOBAL VALUES
SUM_TO_FIND = 2020


# MAIN FUNCTIONS
def part_one():
    memo = set()
    for num in puzzle_input:
        num_to_find = SUM_TO_FIND - num
        if num_to_find in memo:
            return num_to_find * num
        memo.add(num)

def part_two():
    nums = sorted(puzzle_input)
    for i, num in enumerate(nums[:-2]):
        j, k = i+1, len(nums)-1
        while j < k:
            total_sum = num + nums[j] + nums[k]
            if total_sum == SUM_TO_FIND:
                return num * nums[j] * nums[k]
            elif total_sum > SUM_TO_FIND:
                k -= 1
            elif total_sum < SUM_TO_FIND:
                j += 1


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
