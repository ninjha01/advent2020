import re

_input = open("four/input.txt").read().split("\n\n")

__input = [re.split(" |\n", x.strip()) for x in _input]
puzzle = []
for x in __input:
    z = {}
    for y in x:
        try:
            k, v = y.split(":")
            z[k] = v
        except:
            pass
    puzzle.append(z)


def part_one():
    required_keys = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        #   "cid",
    ]
    count = 0
    for x in puzzle:
        valid = True
        for k in required_keys:
            if k not in list(x.keys()):
                valid = False
                break
        if valid:
            count += 1
    return count


def part_two():
    def byr(x):
        assert len(x) == 4
        assert int(x) >= 1920 and int(x) <= 2002

    def iyr(x):
        assert len(x) == 4
        assert int(x) >= 2010 and int(x) <= 2020

    def eyr(x):
        assert len(x) == 4
        assert int(x) >= 2020 and int(x) <= 2030

    def hgt(x):
        if x[-2:] == "cm":
            assert int(x[:-2]) >= 150 and int(x[:-2]) <= 193
        elif x[-2:] == "in":
            assert int(x[:-2]) >= 59 and int(x[:-2]) <= 76
        else:
            assert False

    def hcl(x):
        assert x[0] == "#"
        assert re.match("[0-9a-f]{6}$", x[1:])

    def ecl(x):
        assert x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def pid(x):
        assert re.match("[0-9]{9}$", x)

    required_keys = {
        "byr": byr,
        "iyr": iyr,
        "eyr": eyr,
        "hgt": hgt,
        "hcl": hcl,
        "ecl": ecl,
        "pid": pid,
        #   "cid",
    }
    count = 0
    for x in puzzle:
        valid = True
        for k, v in required_keys.items():
            if k not in list(x.keys()):
                valid = False
                break
            try:
                v(x[k])
            except:
                valid = False
                break
        if valid:
            count += 1
    return count


print(part_one())
print(part_two())
