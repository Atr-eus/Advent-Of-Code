first, second = open(0).read().strip().split("\n\n")

patterns = {p for p in first.split(", ")}
designs = [d for d in second.splitlines()]
m = max(len(p) for p in patterns)

cache = {}


def get_ways(d) -> int:
    if d == "":
        return 1
    if d in cache:
        return cache[d]
    c = 0
    for k in range(min(m, len(d)) + 1):
        if d[:k] in patterns:
            c += get_ways(d[k:])
    cache[d] = c
    return c


print(sum(get_ways(d) for d in designs))
