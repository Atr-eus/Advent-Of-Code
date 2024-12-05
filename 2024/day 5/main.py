import sys

lines = (line.rstrip() for line in sys.stdin)

rules = []
for line in lines:
    if line == "":
        break
    else:
        rules += [tuple(map(int, line.split("|")))]

pages = [list(map(int, line.split(","))) for line in lines]

p1 = p2 = 0
for page in pages:
    rep = ok = True
    while rep:
        rep = False
        for a, b in rules:
            if a not in page or b not in page:
                continue
            i = page.index(a)
            j = page.index(b)
            if i < j:
                continue

            rep = True
            ok = False

            page[i] ^= page[j]
            page[j] ^= page[i]
            page[i] ^= page[j]

    if ok:
        p1 += page[len(page) // 2]
    else:
        p2 += page[len(page) // 2]

print(p1, p2)
