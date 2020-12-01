with open('input.txt', 'r') as file:
    puzzle_input = [int(number_line) for number_line in file]

SUM_TO_FIND = 2020

def find_two_sum():
    memo = set()
    for num in puzzle_input:
        num_to_find = SUM_TO_FIND - num
        if num_to_find in memo:
            return num_to_find * num
        memo.add(num)

def find_three_sum():
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

print('Part 1:', find_two_sum())
print('Part 2:', find_three_sum())
