_input = open("eleven/input.txt").readlines()
puzzle = [list(x.strip()) for x in _input]


def part_one():
    def get_next_state(i, j, puzzle):
        seat = puzzle[i][j]
        adjacent = [
            (a, b)
            for a, b in [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
                (i - 1, j - 1),
                (i - 1, j + 1),
                (i + 1, j - 1),
                (i + 1, j + 1),
            ]
            if a >= 0 and a < len(puzzle) and b >= 0 and b < len(puzzle[0])
        ]
        val = seat
        if seat == "L" and all(
            [puzzle[a][b] == "L" or puzzle[a][b] == "." for a, b in adjacent]
        ):
            val = "#"
        if seat == "#":
            count = 0
            for a, b in adjacent:
                if puzzle[a][b] == "#":
                    count += 1
            if count >= 4:
                val = "L"
        return val

    prev_state = []
    next_state = puzzle
    while prev_state != next_state:
        prev_state = next_state
        next_state = [
            [get_next_state(a, b, prev_state) for b in range(len(puzzle[0]))]
            for a in range(len(puzzle))
        ]

    count = 0
    for x in sum(prev_state, []):
        if x == "#":
            count += 1

    print(count)


def pprint(x):
    for y in x:
        print("".join(y))


def part_two():
    def get_next_state(i, j, puzzle):
        seat = puzzle[i][j]
        directions = [
            (lambda c: (c[0] + 1, c[1]), "north"),
            (lambda c: (c[0] - 1, c[1]), "south"),
            (lambda c: (c[0], c[1] + 1), "east"),
            (lambda c: (c[0], c[1] - 1), "west"),
            (lambda c: (c[0] + 1, c[1] - 1), "nw"),
            (lambda c: (c[0] + 1, c[1] + 1), "ne"),
            (lambda c: (c[0] - 1, c[1] - 1), "sw"),
            (lambda c: (c[0] - 1, c[1] + 1), "se"),
        ]

        if seat == "L":
            for d, l in directions:
                ni, nj = d((i, j))
                while ni >= 0 and ni < len(puzzle) and nj >= 0 and nj < len(puzzle[0]):
                    if puzzle[ni][nj] == "#":
                        return "L"
                    elif puzzle[ni][nj] == "L":
                        ni, nj = -1, -1
                    else:
                        ni, nj = d((ni, nj))
            return "#"
        elif seat == "#":
            count = 0
            for d, l in directions:
                ni, nj = d((i, j))
                while ni >= 0 and ni < len(puzzle) and nj >= 0 and nj < len(puzzle[0]):
                    if puzzle[ni][nj] == "#":
                        count += 1
                        if count >= 5:
                            return "L"
                        ni, nj = -1, -1
                    elif puzzle[ni][nj] == "L":
                        ni, nj = -1, -1
                    else:
                        ni, nj = d((ni, nj))
            return "#"
        else:
            return seat

    prev_state = []
    next_state = puzzle
    i = 0
    while prev_state != next_state:
        prev_state = next_state
        i += 1
        next_state = [
            [get_next_state(a, b, prev_state) for b in range(len(puzzle[0]))]
            for a in range(len(puzzle))
        ]

    count = 0
    for x in sum(prev_state, []):
        if x == "#":
            count += 1

    print(count)


part_two()
