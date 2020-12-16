from collections import defaultdict

_input = open("fifteen/input.txt").read().split(",")
puzzle = [int(x) for x in _input]


def part_one(puzzle, N=2020):
    when_said_map = defaultdict(lambda: [])
    turn_map = {}
    for i, p in enumerate(puzzle):
        turn = i + 1
        when_said_map[p].append(turn)
        turn_map[turn] = p
    # print(turn_map)
    last_num = puzzle[-1]
    for turn in range(len(puzzle) + 1, N + 1):

        if len(when_said_map[last_num]) == 0 or (
            len(when_said_map[last_num]) == 1 and turn_map[turn - 1] == last_num
        ):
            turn_map[turn] = 0
            # print("Last num", last_num, "say", turn_map[turn])
            last_num = 0
            when_said_map[last_num].append(turn)
        else:
            to_say = when_said_map[last_num][-1] - when_said_map[last_num][-2]
            turn_map[turn] = 0 if to_say <= 0 else to_say
            # print("Last num", last_num, "say", turn_map[turn])
            last_num = turn_map[turn]
            when_said_map[last_num].append(turn)
    # print(turn_map)
    return turn_map[N]


print(part_one(puzzle, 30000000))
