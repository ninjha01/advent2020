import re

_input = open("./input.txt").readlines()
puzzle = [re.split(" |: ", x.strip()) for x in _input]


def part_one():
    count = 0
    for (quota, letter, pwd) in puzzle:
        _min, _max = [int(x) for x in quota.split("-")]
        count_map = {}
        for x in pwd:
            count_map[x] = count_map.get(x, 0) + 1
        if (
            letter in count_map
            and count_map[letter] >= _min
            and count_map[letter] <= _max
        ):
            count += 1
    print(count)


def part_two():
    count = 0
    for (quota, letter, pwd) in puzzle:
        i, j = [int(x) - 1 for x in quota.split("-")]
        i_corr = pwd[i] == letter
        j_corr = pwd[j] == letter
        if i_corr and not j_corr:
            print(pwd)
            count += 1
        elif not i_corr and j_corr:
            print(pwd)
            count += 1
    print(count)


part_one()
part_two()
