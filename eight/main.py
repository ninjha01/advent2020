import re

_input = open("eight/input.txt").readlines()
puzzle = [x.strip().split(" ") for x in _input]


def part_one(puzzle):
    acc = 0
    pc = 0
    seen = set()
    while pc < len(puzzle):
        ins, sign, arg = puzzle[pc]
        if pc in seen:
            raise ValueError("Revisited", puzzle[pc], "Acc: ", acc)
        seen.add(pc)
        if ins == "nop":
            pc += 1
        elif ins == "jmp":
            increment = int(arg)
            if sign == "-":
                increment *= -1
            pc += increment
        elif ins == "acc":
            increment = int(arg)
            if sign == "-":
                increment *= -1
            acc += increment
            pc += 1
        else:
            raise ValueError("Unknown instruction", puzzle[pc])
    return acc


def part_two():
    nops = [i for i, x in enumerate(puzzle) if x[0] == "nop"]
    jmps = [i for i, x in enumerate(puzzle) if x[0] == "jmp"]
    permutations = []
    for nop_idx in nops:
        perm = puzzle.copy()
        perm[nop_idx] = ["jmp"] + perm[nop_idx][1:]
        permutations.append((f"Swapped nop @ {nop_idx} for jmp", perm))

    for jmp_idx in jmps:
        perm = puzzle.copy()
        perm[jmp_idx] = ["nop"] + perm[jmp_idx][1:]
        permutations.append((f"Swapped jmp @ {jmp_idx} for nop", perm))
    for i, (label, p) in enumerate(permutations):
        succeeded = False
        try:
            res = part_one(p)
            succeeded = True
        except Exception as e:
            pass
        if succeeded:
            print(label, "succeeded, acc: ", res)
            break
