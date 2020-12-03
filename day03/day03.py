from itertools import count
from math import prod

is_tree = lambda c: c == '#'
tree_line = lambda line: list(map(is_tree, line[:31]))

with open('input.txt', 'r') as file:
    tree_map = list(map(tree_line, file))

def trees_hit(tree_map, right, down):
    return sum(
        row[col % len(row)] for row, col
        in zip(tree_map[down::down], count(right, right))
    )

def product_hit(tree_map, *args):
    return prod(trees_hit(tree_map, *arg) for arg in args)

print("Part 1:", trees_hit(tree_map, 3, 1))
print("Part 2:", product_hit(tree_map, (1,1), (3,1), (5,1), (7,1), (1,2)))