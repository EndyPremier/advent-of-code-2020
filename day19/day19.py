import os, re

from utils import get_data, run, map_tuple


# INPUT HELPERS
def split_pattern(pattern):
    return tuple(
        map_tuple(int, chunk.split())
        for chunk in pattern.split(' | ')
    )

def parse_syntax(syntax_input):
    syntaxes = {}
    for syntax in syntax_input.split('\n'):
        index, pattern = syntax.split(': ')
        if pattern[0] == '"':
            pattern = pattern[1:-1]
        else:
            pattern = split_pattern(pattern)
        syntaxes[int(index)] = pattern
    return syntaxes


# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
puzzle_input = get_data(DIR_ROOT)
syntax_input, strings_input = puzzle_input.split('\n\n')

syntax_input  = parse_syntax(syntax_input)
strings_input = strings_input.split()


# HELPER FUNCTIONS

def eval_pattern(index, memo=None):
    if memo is None:
        memo = syntax_input.copy()
    if isinstance(memo[index], str):
        return memo[index]
    new_chunks = []
    for chunks in memo[index]:
        subchunks = (eval_pattern(i, memo) for i in chunks)
        chunk = ''.join(subchunks)
        new_chunks.append(chunk)
    memo[index] = f"({'|'.join(new_chunks)})"
    return memo[index]


# MAIN FUNCTIONS
def part_one():
    pattern = eval_pattern(0)
    return sum(
        bool(re.fullmatch(pattern, string))
        for string in strings_input
    )

def part_two():
    #  8: 42 | 42 8        -> 42+
    # 11: 42 31 | 42 11 31 -> 42+31+ where len(42) == len(31)
    #  0: 8 11             -> 42+31+ where len(42) > len(31)
    this_syntax = syntax_input.copy()
    left_group  = eval_pattern(42, this_syntax)
    right_group = eval_pattern(31, this_syntax)
    pattern = f'({left_group}+)({right_group}+)'
    count = 0
    for string in strings_input:
        match = re.fullmatch(pattern, string)
        if not match:
            continue
        left_match, right_match = match[1], match[149]
        left_count = len(re.findall(left_group, left_match))
        right_count = len(re.findall(right_group, right_match))
        count += left_count > right_count
    return count


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
