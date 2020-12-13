import math

_input = open("thirteen/input.txt").readlines()
timestamp = int(_input[0])
busses = [
    int(x.strip()) if x.strip() != "x" else None for x in _input[1].strip().split(",")
]


def part_one():
    filtered = list(filter(lambda x: bool(x), busses))
    mods = [math.ceil(timestamp / f) * f - timestamp for f in filtered]
    print(min(mods) * filtered[mods.index(min(mods))])


def part_two():
    filtered = list(filter(lambda x: bool(x), busses))
    offsets = [(x, busses.index(x)) for x in filtered]
    inc = 1
    num = 0
    for i in range(len(offsets)):
        while True:
            if all((num + o) % x == 0 for (x, o) in offsets[0 : i + 1]):
                inc *= offsets[i][0]
                break
            else:
                num += inc
    return num


print("Result", part_two())
