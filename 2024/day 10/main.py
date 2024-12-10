# BFS
from collections import deque

grid = [[int(c) for c in l.strip()] for l in open(0)]
n = len(grid)

trailheads = [(x, y) for x in range(n) for y in range(n) if grid[x][y] == 0]


def solve_part1(grid, x, y) -> int:
    q = deque([(x, y)])
    res = 0
    visited = set({x, y})

    while q:
        cx, cy = q.popleft()
        for dx, dy in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
            if (
                dx < 0
                or dx >= n
                or dy < 0
                or dy >= n
                or grid[dx][dy] != grid[cx][cy] + 1
                or (dx, dy) in visited
            ):
                continue
            visited.add((dx, dy))

            if grid[dx][dy] == 9:
                res += 1
            else:
                q.append((dx, dy))

    return res


def solve_part2(grid, x, y) -> int:
    q = deque([(x, y)])
    res = 0
    ways_to_reach = {(x, y): 1}

    while q:
        cx, cy = q.popleft()
        if grid[cx][cy] == 9:
            res += ways_to_reach[(cx, cy)]

        for dx, dy in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
            if (
                dx < 0
                or dx >= n
                or dy < 0
                or dy >= n
                or grid[dx][dy] != grid[cx][cy] + 1
            ):
                continue

            if (dx, dy) in ways_to_reach:
                ways_to_reach[(dx, dy)] += ways_to_reach[(cx, cy)]
                continue
            ways_to_reach[(dx, dy)] = ways_to_reach[(cx, cy)]
            q.append((dx, dy))

    return res


part1 = sum(solve_part1(grid, x, y) for (x, y) in trailheads)
part2 = sum(solve_part2(grid, x, y) for (x, y) in trailheads)
print(part1, part2)
