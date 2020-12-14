_input = open("fourteen/input.txt").readlines()
puzzle = []
for x in _input:
    x = x.strip()
    if "mask" in x:
        puzzle.append(("set mask", x.split(" ")[-1]))
    elif "mem" in x:
        addr, val = x.split("[")[1].split("] = ")
        puzzle.append(("set mem", (int(addr), int(val))))
    else:
        raise ValueError("Unkown ins")


def part_one():
    mask = None
    memory = {}
    for ins, val in puzzle:
        if ins == "set mask":
            mask = val
        elif ins == "set mem":
            addr, _val = val
            bin_val = list(format(_val, "036b"))[::-1]
            for i in range(len(bin_val)):
                m = mask[::-1][i]
                if m == "1":
                    bin_val[i] = "1"
                elif m == "0":
                    bin_val[i] = "0"
                else:
                    assert m == "X"
            memory[addr] = "".join(bin_val[::-1])
        else:
            raise ValueError("Unkown ins")

    _sum = 0
    for v in memory.values():
        _sum += int(v, 2)
    print(_sum)


def part_two():
    def gen_addrs(mask, bin_addr):
        mask = mask[::-1]
        bin_addr = bin_addr[::-1]
        addrs = [[]]
        for i, m in enumerate(mask):
            if m == "0":
                for a in addrs:
                    a.append(bin_addr[i])
            elif m == "1":
                for a in addrs:
                    a.append("1")
            elif m == "X":
                new = []
                for a in addrs:
                    new.extend([a + ["0"], a + ["1"]])
                addrs = new
            else:
                raise ValueError("Invalid", m)
        addrs = [int("".join(a[::-1]), 2) for a in addrs]
        return addrs

    mask = None
    memory = {}
    for ins, val in puzzle:
        if ins == "set mask":
            mask = val
        elif ins == "set mem":
            addr, _val = val
            bin_addr = list(format(addr, "036b"))
            for a in gen_addrs(mask, bin_addr):
                memory[a] = _val
        else:
            raise ValueError("Unkown ins")

    _sum = 0
    for v in memory.values():
        _sum += v
    print(_sum)


part_one()
part_two()
