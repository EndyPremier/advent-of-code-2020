import os, re
from collections import defaultdict, Counter

from utils import get_data, run


# INPUT SECTION
def get_input():
    DIR_ROOT = os.path.dirname(__file__)
    puzzle_input = get_data(DIR_ROOT)
    return puzzle_input


# HELPER FUNCTIONS
FOOD_REGEX = r'(.*) \(contains (.*)\)'


# MAIN FUNCTIONS
def part_one():
    allergy_count = Counter()
    allergy_ingredient = defaultdict(Counter)
    ingredient_count = Counter()

    for ingredient_description in get_input().split('\n'):
        match = re.fullmatch(FOOD_REGEX, ingredient_description)
        ingredients = set(match[1].split())
        allergies = set(match[2].split(', '))
        for allergy in allergies:
            allergy_count[allergy] += 1
        for ingredient in ingredients:
            ingredient_count[ingredient] += 1
            for allergy in allergies:
                allergy_ingredient[allergy][ingredient] += 1

    possible_ingredients = {
        ingredient
        for allergy, ingredients in allergy_ingredient.items()
        for ingredient, count in ingredients.items()
        if count == allergy_count[allergy]
    }

    return sum(
        count
        for ingredient, count in ingredient_count.items()
        if ingredient not in possible_ingredients
    )

def part_two():
    allergy_count = Counter()
    allergy_ingredient_count = defaultdict(Counter)
    ingredient_count = Counter()

    for ingredient_description in get_input().split('\n'):
        match = re.fullmatch(FOOD_REGEX, ingredient_description)
        ingredients = set(match[1].split())
        allergies = set(match[2].split(', '))
        for allergy in allergies:
            allergy_count[allergy] += 1
        for ingredient in ingredients:
            ingredient_count[ingredient] += 1
            for allergy in allergies:
                allergy_ingredient_count[allergy][ingredient] += 1

    allergy_ingredient = {}
    is_definite = []
    for allergy, ingredients in allergy_ingredient_count.items():
        allergy_ingredient[allergy] = {
            ingredient
            for ingredient, count in ingredients.items()
            if count == allergy_count[allergy]
        }
        if len(allergy_ingredient[allergy]) == 1:
            is_definite.append(allergy)
    print(allergy_ingredient)

    while is_definite:
        allergy = is_definite.pop()
        ingredient = allergy_ingredient[allergy].pop()
        allergy_ingredient[allergy] = ingredient
        for other, ingredients in allergy_ingredient.items():
            if isinstance(ingredients, set):
                ingredients -= { ingredient }
                if len(ingredients) == 1:
                    is_definite.append(other)

    return ','.join(
        ingredient for _, ingredient in sorted(allergy_ingredient.items())
    )


# RUNNING FUNCTION
if __name__ == "__main__":
    run(part_one, part_two)
