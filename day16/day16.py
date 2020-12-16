import os, re
from math import prod

from utils import get_data, run, map_tuple


# INPUT SECTION
DIR_ROOT = os.path.dirname(__file__)
puzzle_input = get_data(DIR_ROOT)


# HELPER FUNCTIONS
## Input Extraction
RULE_REGEX = r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)'
def extract_rules(rules):
    ret = {}
    for rule in rules.split('\n'):
        match  = re.match(RULE_REGEX, rule)
        field  = match[1]
        range1 = range(int(match[2]), int(match[3]) + 1)
        range2 = range(int(match[4]), int(match[5]) + 1)
        ret[field] = (range1, range2)
    return ret

def extract_tickets(tickets):
    return [
        map_tuple(int, ticket.split(','))
        for ticket in tickets.split('\n')[1:]
    ]

def extract_input():
    rules, this_ticket, other_tickets = puzzle_input.split('\n\n')
    rules = extract_rules(rules)
    this_ticket = extract_tickets(this_ticket)[0]
    other_tickets = extract_tickets(other_tickets)
    return rules, this_ticket, other_tickets


## Validation
def value_in_ranges(value, rule):
    return any(value in range_ for range_ in rules[rule])

def is_valid_ticket(ticket):
    return all(
        any(value_in_ranges(value, rule) for rule in rules)
        for value in ticket
    )


## Validation
def get_possibilities():
    possibilities = [
        { rule for rule in rules if value_in_ranges(value, rule) }
        for value in this_ticket
    ]
    filtered_tickets = filter(is_valid_ticket, other_tickets)
    for ticket in filtered_tickets:
        for i, value in enumerate(ticket):
            possibilities[i] &= {
                rule for rule in possibilities[i]
                if value_in_ranges(value, rule)
            }
    return possibilities

def reduce_possibilities(poss):
    unambiguous = set(i for i, val in enumerate(poss) if len(val) == 1)
    ambiguous = set(i for i, _ in enumerate(poss) if i not in unambiguous)
    for i in unambiguous:
        poss[i] = poss[i].pop()
    while ambiguous:
        i = unambiguous.pop()
        for j in ambiguous:
            poss[j].remove(poss[i])
            if len(poss[j]) == 1:
                unambiguous.add(j)
                poss[j] = poss[j].pop()
        ambiguous -= unambiguous
    return poss


# GLOBAL VALUES
rules, this_ticket, other_tickets = extract_input()


# MAIN FUNCTIONS
def part_one():
    return sum(
        value for ticket in other_tickets for value in ticket
        if all(not value_in_ranges(value, rule) for rule in rules)
    )

def part_two():
    possibilities = get_possibilities()
    fields = reduce_possibilities(possibilities)

    return prod(
        val for field, val in zip(fields, this_ticket) if 'departure' in field
    )


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
