xinput = open("./input.txt").readlines()
_input = [int(x) for x in xinput]


def part_one(_input):
    goal = 2020
    number_map = {k: True for k in _input}
    for k in number_map.keys():
        if goal - k in number_map:
            return (k, goal - k)


x, y = part_one(_input)

print("Part 1", x * y)


def part_two(_input):
    goal = 2020
    number_map = {k: True for k in _input}
    for k in number_map.keys():
        remainder = goal - k
        for j in number_map.keys():
            if remainder - j in number_map:
                if k + j + remainder - j == goal:
                    print(k * j * (remainder - j))
                    break


part_two(_input)
