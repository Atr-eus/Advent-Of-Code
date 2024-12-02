def is_safe(levs: list[int]) -> bool:
    inc_safe = [
        levs[i + 1] > levs[i] and (levs[i + 1] - levs[i]) <= 3
        for i in range(0, len(levs) - 1)
    ]
    dec_safe = [
        levs[i + 1] < levs[i] and (levs[i] - levs[i + 1]) <= 3
        for i in range(0, len(levs) - 1)
    ]

    # either the increasing list or the decreasing list must have "True" values only
    return all(inc_safe) or all(dec_safe)


def solve_part1() -> int:
    input = []

    with open("./input.txt") as input_file:
        lines = input_file.readlines()
        for line in lines:
            input.append(list(map(int, line.split())))

    res = 0
    for levs in input:
        if is_safe(levs):
            res += 1

    return res


def solve_part2() -> int:
    input = []

    with open("./input.txt") as input_file:
        lines = input_file.readlines()
        for line in lines:
            input.append(list(map(int, line.split())))

    res = 0
    for levs in input:
        if is_safe(levs):
            res += 1
            continue

        for i, _ in enumerate(levs):
            if is_safe(levs[:i] + levs[i + 1 :]):
                res += 1
                break

    return res


print(solve_part1(), solve_part2())
