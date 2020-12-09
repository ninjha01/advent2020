_input = open("nine/input.txt").readlines()
puzzle = [int(x.strip()) for x in _input]


def part_one():
    def is_valid(number, prev25):
        assert len(prev25) == 25
        prev_dict = {k: True for k in prev25}
        for k in prev_dict.keys():
            if (number - k) in prev_dict and (number - k) is not k:
                return True
        return False

    i = 25
    while i < len(puzzle):
        if is_valid(puzzle[i], puzzle[i - 25 : i]):
            pass
        else:
            return puzzle[i]
        i += 1
    raise ValueError("Failed!")


print(part_one())


def part_two(invalid_num):
    i = 0
    j = 1
    while j < len(puzzle):
        total = sum(puzzle[i : j + 1])
        if total == invalid_num:
            _slice = puzzle[i : j + 1]
            return min(_slice) + max(_slice)
        elif total > invalid_num:
            i += 1
        elif total < invalid_num:
            j += 1
    raise ValueError("Failed")


print(part_two(part_one()))
