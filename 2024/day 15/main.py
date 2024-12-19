first, second = open(0).read().strip().split("\n\n")
grid = [list(l) for l in first.splitlines()]
moves = second.replace("\n", "")

p2cng = {"#": "##", "O": "[]", ".": "..", "@": "@."}
p2grid = [list("".join(p2cng[c] for c in l)) for l in first.splitlines()]

n = len(grid)
for i in p2grid:
    print(*i, sep="")
rx, ry = 0, 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == "@":
            rx, ry = i, j
            break

mx = {"^": -1, "v": 1}
my = {"<": -1, ">": 1}
for mov in moves:
    x = mx.get(mov, 0)
    y = my.get(mov, 0)

    crx, cry = rx, ry
    to_move = []
    flag = True
    while True:
        crx += x
        cry += y
        cc = grid[crx][cry]

        if cc == "#":
            flag = False
            break
        elif cc == "O":
            to_move.append((crx, cry))
        elif cc == ".":
            break

    if flag:
        grid[rx][ry] = "."
        grid[rx + x][ry + y] = "@"
        for i, j in to_move:
            grid[i + x][j + y] = "O"
        rx += x
        ry += y

part1 = sum(x * 100 + y for x in range(n) for y in range(n) if grid[x][y] == "O")

print(part1)
