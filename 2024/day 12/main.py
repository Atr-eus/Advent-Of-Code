from collections import deque

inp = [line.strip() for line in open(0)]
n = len(inp)

regions = list()
visited = set()


def get_edges(x: int, y: int) -> list[tuple[int, int]]:
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]


def get_corners(x: int, y: int) -> list[tuple[float, float]]:
    return [
        (x - 0.5, y - 0.5),
        (x + 0.5, y - 0.5),
        (x + 0.5, y + 0.5),
        (x - 0.5, y + 0.5),
    ]


def get_area(region: set[tuple[int, int]]) -> int:
    return len(region)


def get_perimeter(region: set[tuple[int, int]]) -> int:
    res = 0

    for x, y in region:
        res += 4
        for dx, dy in get_edges(x, y):
            if (dx, dy) in region:
                res -= 1
    return res


def get_side_count(region: set[tuple[int, int]]) -> int:
    res = 0
    cc = set()
    for x, y in region:
        for dx, dy in get_corners(x, y):
            cc.add((dx, dy))

    for dx, dy in cc:
        corner_sq_in_region: list[int] = [
            (i, j) in region for i, j in get_corners(dx, dy)
        ]
        k = sum(corner_sq_in_region)

        if k == 1 or k == 3:
            res += 1
        elif k == 2 and (
            corner_sq_in_region == [1, 0, 1, 0] or corner_sq_in_region == [0, 1, 0, 1]
        ):
            res += 2

    return res


for x in range(n):
    for y in range(n):
        if (x, y) in visited:
            continue
        visited.add((x, y))
        curr_region = set()
        curr_region.add((x, y))

        q = deque()
        q.append((x, y))
        while q:
            cx, cy = q.popleft()
            for dx, dy in get_edges(cx, cy):
                if (
                    dx < 0
                    or dx >= n
                    or dy < 0
                    or dy >= n
                    or inp[x][y] != inp[dx][dy]
                    or (dx, dy) in curr_region
                ):
                    continue
                curr_region.add((dx, dy))
                q.append((dx, dy))
        visited |= curr_region
        regions.append(curr_region)

part1 = sum(get_area(region) * get_perimeter(region) for region in regions)
part2 = sum(get_area(region) * get_side_count(region) for region in regions)
print(part1, part2)
