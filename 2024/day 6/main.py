import sys

lines = sys.stdin.read().splitlines()

n = len(lines)
x, y = 0, 0
d = ""
for i in range(n):
    for j in range(n):
        if lines[i][j] == "^":
            x, y = i, j
            d = lines[i][j]
init_x, init_y = x, y


def is_a_loop(x, y):
    pos = (x, y)
    state = d
    i, j = init_x, init_y
    corners_rec = set()
    while i != 0 and i != n - 1 and j != 0 and j != n - 1:
        if state == "^":
            if lines[i - 1][j] == "#" or (i - 1, j) == pos:
                state = ">"
                corner = (i - 1, j, state)

                if corner in corners_rec:
                    return True
                corners_rec.add(corner)
                continue
            i -= 1
        elif state == ">":
            if lines[i][j + 1] == "#" or (i, j + 1) == pos:
                state = "v"
                corner = (i, j + 1, state)

                if corner in corners_rec:
                    return True
                corners_rec.add(corner)
                continue
            j += 1
        elif state == "v":
            if lines[i + 1][j] == "#" or (i + 1, j) == pos:
                state = "<"
                corner = (i + 1, j, state)

                if corner in corners_rec:
                    return True
                corners_rec.add(corner)
                continue
            i += 1
        else:
            if lines[i][j - 1] == "#" or (i, j - 1) == pos:
                state = "^"
                corner = (i, j - 1, state)

                if corner in corners_rec:
                    return True
                corners_rec.add(corner)
                continue
            j -= 1
    return False


res = 0
for i in range(n):
    for j in range(n):
        if (i, j) != (x, y) and lines[i][j] == ".":
            res += is_a_loop(i, j)

print(res)
