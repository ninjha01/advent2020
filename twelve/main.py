import math

_input = open("twelve/input.txt").readlines()
puzzle = [(x[0], int(x[1:-1])) for x in _input]


def part_one():
    angle = float(0)
    x, y = float(0), float(0)

    def to_rad(x):
        return x / 360 * 2 * math.pi

    for (op, val) in puzzle:
        if op == "F":
            x += math.cos(to_rad(angle)) * val
            y += math.sin(to_rad(angle)) * val
        elif op == "N":
            y += val
        elif op == "S":
            y -= val
        elif op == "E":
            x += val
        elif op == "W":
            x -= val
        elif op == "L":
            angle += val
        elif op == "R":
            angle -= val
    print("Part one", abs(x) + abs(y))


def part_two():
    sx, sy = float(0), float(0)
    dx, dy = float(10), float(1)

    def to_rad(x):
        return x / 360 * 2 * math.pi

    def to_deg(x):
        return x / (2 * math.pi) * 360

    for (op, val) in puzzle:
        if op == "F":
            sx += dx * val
            sy += dy * val
        elif op == "N":
            dy += val
        elif op == "S":
            dy -= val
        elif op == "E":
            dx += val
        elif op == "W":
            dx -= val
        elif op == "L":
            if val == 90:
                dx, dy = -dy, dx
            elif val == 180:
                dx, dy = -dx, -dy
            elif val == 270:
                dx, dy = dy, -dx
        elif op == "R":
            if val == 90:
                dx, dy = dy, -dx
            elif val == 180:
                dx, dy = -dx, -dy
            elif val == 270:
                dx, dy = -dy, dx
        else:
            raise ValueError("Unexpected op")
    print("Part two", round(abs(sx)) + round(abs(sy)))


part_one()
part_two()
