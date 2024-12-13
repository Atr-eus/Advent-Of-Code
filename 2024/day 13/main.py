import re

part1, part2 = 0, 0


def get_intersection(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> tuple:
    i = (x3 * y2 - y3 * x2) / (x1 * y2 - y1 * x2)
    j = (x3 - x1 * i) / x2

    return (i, j)


for b in open(0).read().split("\n\n"):
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", b))

    # part 1
    i, j = get_intersection(ax, ay, bx, by, px, py)
    if int(i) == i and int(j) == j:
        part1 += i * 3 + j

    # part 2
    px += 10000000000000
    py += 10000000000000

    i, j = get_intersection(ax, ay, bx, by, px, py)
    if int(i) == i and int(j) == j:
        part2 += i * 3 + j

print(int(part1), int(part2))
