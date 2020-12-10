_input = open("ten/input.txt").readlines()
puzzle = [int(x.strip()) for x in _input]


def part_one(puzzle):
    def get_full_chain():
        max_adapter = max(puzzle)
        device = max_adapter + 3
        jc = [0]
        adapter_set = sorted(puzzle)
        for a in adapter_set:
            if jc[-1] + 3 == device:
                assert len(jc) == len(adapter_set + [0])
                return jc
            possibilities = [jc[-1] + 1, jc[-1] + 2, jc[-1] + 3]
            for p in possibilities:
                if p in adapter_set:
                    jc.append(p)
                    continue

    full_chain = get_full_chain()
    diffs = {}
    for i in range(len(full_chain) - 1):
        curr = full_chain[i]
        _next = full_chain[i + 1]
        diffs[_next - curr] = diffs.get(_next - curr, 0) + 1
        diffs[3] = diffs.get(3, 0) + 1
    return diffs[3] * diffs[1]


print(part_one(puzzle))


def part_two(puzzle):
    path_counts = {k: 0 for k in [0] + puzzle + [max(puzzle) + 3]}
    path_counts[0] = 1
    for v in sorted(list(path_counts.keys())):
        possibilities = [v + 1, v + 2, v + 3]
        for p in possibilities:
            if p in puzzle + [max(puzzle) + 3]:
                path_counts[p] += path_counts[v]
    return path_counts[max(puzzle) + 3]


print(part_two(puzzle))
