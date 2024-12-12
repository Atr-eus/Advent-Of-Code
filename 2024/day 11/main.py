stones = list(map(int, input().split()))


def dig_c(n: int) -> int:
    if n == 0:
        return 0
    else:
        return 1 + dig_c(n // 10)


memo = {}

for st in stones:
    memo.setdefault(st, 0)
    memo[st] += 1

# print(memo.items())

for i in range(75):
    curr_memo = {}

    for j, k in memo.items():
        len = dig_c(j)

        if j == 0:
            curr_memo.setdefault(1, 0)
            curr_memo[1] += k
        elif len % 2 == 0:
            l = int(str(j)[: len // 2])
            r = int(str(j)[len // 2 :])
            curr_memo.setdefault(l, 0)
            curr_memo.setdefault(r, 0)
            curr_memo[l] += k
            curr_memo[r] += k
        else:
            curr_memo.setdefault(j * 2024, 0)
            curr_memo[j * 2024] += k

    memo = curr_memo

part2 = sum(memo.values())
print(part2)
