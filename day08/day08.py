import os

from utils import get_data, map_list


# INPUT HELPERS
def get_op(line):
    op, arg = line.split()
    return [op, int(arg)]

# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
instructions = map_list(get_op, get_data(DIR_ROOT).split('\n'))


# HELPER FUNCTIONS
def run_op(line, val):
    op, arg = instructions[line]
    line += arg if op == 'jmp' else 1
    val  += arg if op == 'acc' else 0
    return line, val

def switch_op(instructions, line):
    old_op = instructions[line][0]
    new_op = 'nop' if old_op == 'jmp' else 'jmp'
    instructions[line][0] = new_op


# MAIN FUNCTIONS
def part_one():
    line_ran = set()
    line = acc = 0
    while line not in line_ran and line < len(instructions):
        line_ran.add(line)
        line, acc = run_op(line, acc)
    return acc

def part_two():
    curr_instructions = instructions[::]
    prev_line = None
    traceback_stack = []
    line_ran = set()
    line = acc = 0
    while line < len(curr_instructions):
        # RUN FALLBACK
        if line in line_ran:
            if prev_line is not None:
                switch_op(curr_instructions, prev_line)
            line_ran, line, acc = traceback_stack.pop()
            switch_op(curr_instructions, line)
            prev_line = line
        # ADD TRACEBACK
        else:
            op, arg = curr_instructions[line]
            if op in 'jmp nop' and arg != 1:
                traceback = (line_ran.copy(), line, acc)
                traceback_stack.append(traceback)
        # RUN OP
        line_ran.add(line)
        line, acc = run_op(line, acc)
    return acc


# RUNNING FUNCTION
if __name__ == "__main__":
    print('Part 1:', part_one())
    print('Part 2:', part_two())
