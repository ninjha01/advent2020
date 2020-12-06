import re

_input = open("six/input.txt").read().split("\n\n")
puzzle = [x.split("\n") for x in _input]


def part_one():
    counts = []
    for x in puzzle:
        seen = set()
        for survey in x:
            for q in list(survey):
                seen.add(q)
        counts.append(len(seen))
    return sum(counts)


print(part_one())


def part_two():
    result = 0
    for x in puzzle:
        num_people = len(x)
        seen = {}
        for survey in x:
            for q in list(survey):
                seen[q] = seen.get(q, 0) + 1
        result += len([q for q, count in seen.items() if count == num_people])
    return result


print(part_two())
