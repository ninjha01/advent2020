import re

_input = open("seven/input.txt").readlines()
__input = [x.replace(".", "").replace("bags", "").replace("bag", "") for x in _input]
___input = [re.split("contain|,", x.strip()) for x in __input]
____input = [[y.strip() for y in x] for x in ___input]
puzzle = {x[0]: x[1:] for x in ____input}


def part_one():
    can_get_to_gold = set("shiny gold")

    def contains_gold(bag):
        try:
            contents = [" ".join(bag.split(" ")[1:]) for bag in puzzle[bag]]
        except KeyError:
            return False

        if "shiny gold" in contents:
            can_get_to_gold.add(bag)
            return True
        if bag in can_get_to_gold:
            can_get_to_gold.add(bag)
            return True
        contains = False
        for b in contents:
            if contains_gold(b):
                can_get_to_gold.add(bag)
                contains = True
        return contains

    count = 0
    for p in puzzle:
        if contains_gold(p):
            count += 1
            print(p, True)
        else:
            print(p, False)

    print(count)


def part_two():
    def count_inner_bags(bag):
        count = 0
        try:
            contents = puzzle[bag]
        except KeyError:
            return 0
        for c in contents:
            num, _bag = c.split(" ")[0], " ".join(c.split(" ")[1:])
            try:
                num = int(num)
                count += num
                count += num * count_inner_bags(_bag)
            except ValueError:
                return 0
        return count

    shiny_count = count_inner_bags("shiny gold")
    print(shiny_count)


part_two()
