_input = open("sixteen/input.txt").readlines()
puzzle = {"rules": {}, "nearby_tickets": []}
i = 0
while i < len(_input):
    x = _input[i]
    if "your ticket:" in x:
        puzzle["my ticket"] = _input[i + 1].strip()
        i += 2
    elif "nearby tickets:" in x:
        i += 1
        continue
    elif ":" in x:
        name, ranges = x.strip().split(": ")
        range_1, range_2 = ranges.split(" or ")
        puzzle["rules"][name] = (range_1, range_2)
    elif "," in x:
        puzzle["nearby_tickets"].append(x.strip())
    i += 1


def part_one():
    invalids = []
    for t in puzzle["nearby_tickets"]:
        for x in t.split(","):
            x = int(x)
            valid_for_any = False
            for r in puzzle["rules"].values():
                min_1, max_1 = r[0].split("-")
                min_2, max_2 = r[1].split("-")
                range_1_valid = x >= int(min_1) and x <= int(max_1)
                range_2_valid = x >= int(min_2) and x <= int(max_2)
                if range_1_valid or range_2_valid:
                    valid_for_any = True
                    break
            if not valid_for_any:
                invalids.append(x)
    return sum(invalids)


def part_two():
    field_possiblities = {
        x: set(range(len(puzzle["my ticket"].split(","))))
        for x in puzzle["rules"].keys()
    }

    def is_valid(t):
        for x in t.split(","):
            x = int(x)
            valid_for_any = False
            for r in puzzle["rules"].values():
                min_1, max_1 = r[0].split("-")
                min_2, max_2 = r[1].split("-")
                range_1_valid = x >= int(min_1) and x <= int(max_1)
                range_2_valid = x >= int(min_2) and x <= int(max_2)
                if range_1_valid or range_2_valid:
                    valid_for_any = True
                    break
            if not valid_for_any:
                return False
        return True

    filtered = filter(is_valid, puzzle["nearby_tickets"])
    for f in filtered:
        for i, x in enumerate(f.split(",")):
            x = int(x)
            for name, ranges in puzzle["rules"].items():
                min_1, max_1 = ranges[0].split("-")
                min_2, max_2 = ranges[1].split("-")
                range_1_valid = x >= int(min_1) and x <= int(max_1)
                range_2_valid = x >= int(min_2) and x <= int(max_2)
                if not (range_1_valid or range_2_valid):
                    field_possiblities[name].remove(i)
    while sum([len(v) for v in field_possiblities.values()]) > len(field_possiblities):
        for k1, v1 in field_possiblities.items():
            if len(v1) == 1:
                v1 = list(v1)[0]
                for k2, v2 in field_possiblities.items():
                    if k1 != k2 and v1 in v2:
                        field_possiblities[k2].remove(v1)
    product = 1
    my_ticket = [int(x) for x in puzzle["my ticket"].split(",")]
    for k, v in field_possiblities.items():
        if "departure" in k:
            product *= my_ticket[list(v)[0]]
    return product


print(part_one())
print(part_two())
