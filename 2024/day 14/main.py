import re

width = 101
height = 103

q1, q2, q3, q4 = 0, 0, 0, 0

for l in open(0).read().strip().split("\n"):
    px, py, vx, vy = map(int, re.findall(r"-?\d+", l))

    px += vx * 100
    py += vy * 100

    # wrap around
    px %= width
    py %= height

    # check quadrant
    if px < (width - 1) // 2 and py < (height - 1) // 2:
        q1 += 1
    elif px > (width - 1) // 2 and py < (height - 1) // 2:
        q2 += 1
    elif px < (width - 1) // 2 and py > (height - 1) // 2:
        q3 += 1
    elif px > (width - 1) // 2 and py > (height - 1) // 2:
        q4 += 1

part1 = q1 * q2 * q3 * q4
print(part1)
