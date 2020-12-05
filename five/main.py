import re
import math

_input = open("five/input.txt").readlines()

rows = [0, 127]
cols = [0, 7]


def to_cart(x, i, rows, cols):
    print(i, x[i], rows, cols)
    if x[i] == "B":
        mid = math.ceil((rows[0] + rows[1]) / 2)
        return to_cart(x, i + 1, [mid, rows[1]], cols)
    if x[i] == "F":
        mid = math.floor((rows[0] + rows[1]) / 2)
        return to_cart(x, i + 1, [rows[0], mid], cols)
    if x[i] == "L":
        # HACK
        if x[i - 1] == "F":
            rows[1] = rows[0]
        if x[i - 1] == "B":
            rows[0] = rows[1]
        mid = math.floor((cols[0] + cols[1]) / 2)
        # HACK
        if i + 1 == len(x):
            return rows[0], cols[0]
        return to_cart(x, i + 1, rows, [cols[0], mid])
    if x[i] == "R":
        # HACK
        if x[i - 1] == "F":
            rows[1] = rows[0]
        if x[i - 1] == "B":
            rows[0] = rows[1]
        # HACK
        if i + 1 == len(x):
            return rows[0], cols[1]
        mid = math.ceil((cols[0] + cols[1]) / 2)
        return to_cart(x, i + 1, rows, [mid, cols[1]])


max_val = 0
for _pass in _input:
    x, y = to_cart(_pass.strip(), 0, rows=rows, cols=cols)
    val = x * 8 + y
    if val > max_val:
        max_val = val

print(max_val)

ids = [
    x * 8 + y
    for x, y in [to_cart(_pass.strip(), 0, rows=rows, cols=cols) for _pass in _input]
]

id_map = {k: True for k in ids}

seen_map = set(range(0, max_val + 1))
for x in id_map:
    seen_map.remove(x)

for k in seen_map:
    if k + 1 in id_map and k - 1 in id_map:
        print(k)
