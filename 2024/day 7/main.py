from sys import stdin
from itertools import product

inp = stdin.readlines()


def part1(inp: list[str]) -> int:
    eqns = {}
    for line in inp:
        res, vals = line.split(":")
        eqns[int(res)] = list(map(int, vals.split()))
    ops = ["+", "*"]
    ans = 0

    for res in eqns:
        vals = eqns[res]
        ok = False
        for combo in product(ops, repeat=len(vals) - 1):
            curr = vals[0]
            for i, op in enumerate(combo):
                if op == "+":
                    curr += vals[i + 1]
                elif op == "*":
                    curr *= vals[i + 1]
            if curr == res:
                ok = True
                break
        if ok:
            ans += res

    return ans


def part2(inp: list[str]) -> int:
    eqns = {}
    for line in inp:
        res, vals = line.split(":")
        eqns[int(res)] = list(map(int, vals.split()))

    ops = ["+", "*", "|"]
    ans = 0

    for res in eqns:
        vals = eqns[res]
        ok = False
        for combo in product(ops, repeat=len(vals) - 1):
            curr = vals[0]
            for i, op in enumerate(combo):
                if op == "+":
                    curr += vals[i + 1]
                elif op == "*":
                    curr *= vals[i + 1]
                elif op == "|":
                    curr *= 10 ** len(str(vals[i + 1]))
                    curr += vals[i + 1]
            if curr == res:
                ok = True
                break
        if ok:
            ans += res

    return ans


print(part1(inp), part2(inp))
