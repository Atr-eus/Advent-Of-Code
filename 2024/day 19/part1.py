first, second = open(0).read().strip().split("\n\n")

patterns = {p for p in first.split(", ")}
designs = [d for d in second.splitlines()]
m = max(len(p) for p in patterns)

cache = {}


def can_get(d) -> bool:
    if d == "":
        return True
    if d in cache:
        return cache[d]
    for k in range(min(m, len(d)) + 1):
        if d[:k] in patterns and can_get(d[k:]):
            cache[d] = True
            return True
    cache[d] = False
    return False


print(sum(can_get(d) for d in designs))
