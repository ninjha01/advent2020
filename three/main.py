_input = open("three/input.txt").readlines()
puzzle = [list(x.strip()) for x in _input]


def part_one(slope):
    count = 0
    i = 0
    j = 0
    while True:
        _j = j % len(puzzle[0])
        if puzzle[i][_j] == "#":
            count += 1
        i += slope[0]
        if i >= len(puzzle):
            break
        j += slope[1]
    return count


print(part_one((1, 3)))


def part_two():
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    counts = [part_one(s) for s in slopes]
    x = 1
    for c in counts:
        x = x * c
    return x


part_two()
