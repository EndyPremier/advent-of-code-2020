import os
from math import gcd

from utils import get_data


# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
start_time, buses = get_data(DIR_ROOT).split()
start_time = int(start_time)
buses = {
    int(bus): i
    for i, bus in enumerate(buses.split(','))
    if bus != 'x'
}


# HELPER FUNCTIONS
def lcm(*nums):
    if len(nums) == 0:
        return 1
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        a, b = nums
        return a * b // gcd(a, b)
    return lcm(nums[0], lcm(*nums[1:]))


# MAIN FUNCTIONS
def part_one():
    min_time = None
    best_bus = None
    for bus in buses:
        bus = bus
        ttb = (bus - start_time % bus) % bus
        if min_time is None or ttb < min_time:
            min_time, best_bus = ttb, bus
    return best_bus * min_time

def part_two():
    longest_bus = max(buses)
    curr_increment = longest_bus
    curr_t = longest_bus - buses[longest_bus]
    had_found = { longest_bus }
    to_check = set(bus for bus in buses if bus != longest_bus)
    while to_check:
        found = set(
            bus for bus in to_check
            if (curr_t + buses[bus]) % bus == 0
        )
        curr_increment = lcm(curr_increment, *found)
        to_check -= found
        had_found |= found
        if not to_check:
            return curr_t
        curr_t += curr_increment


# RUNNING FUNCTION
if __name__ == "__main__":
    print('Part 1:', part_one())
    print('Part 2:', part_two())
