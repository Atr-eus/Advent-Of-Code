from sys import stdin
from itertools import product, combinations

inp = [[*line] for line in stdin.read().strip().splitlines()]
n = len(inp)
idx_pairs = set(product(list(range(n)), repeat=2))
ants = {}
antinodes_rec_part1, antinodes_rec_part2 = set(), set()


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


for x, y in idx_pairs:
    if inp[x][y] != ".":
        ants.setdefault(inp[x][y], []).append((x, y))

for occurs in ants.values():
    for p, q in combinations(occurs, 2):
        diff_x = p[0] - q[0]
        diff_y = p[1] - q[1]

        # PART 1
        antinode_pos_1 = (p[0] + diff_x, p[1] + diff_y)
        antinode_pos_2 = (q[0] - diff_x, q[1] - diff_y)
        if antinode_pos_1 in idx_pairs:
            antinodes_rec_part1.add(antinode_pos_1)
        if antinode_pos_2 in idx_pairs:
            antinodes_rec_part1.add(antinode_pos_2)

        # PART 2
        coord_gcd = gcd(diff_x, diff_y)
        diff_x //= coord_gcd
        diff_y //= coord_gcd

        k = 0
        antinode_pos_1 = (p[0] + diff_x * k, p[1] + diff_y * k)
        while antinode_pos_1 in idx_pairs:
            antinodes_rec_part2.add(antinode_pos_1)
            antinode_pos_1 = (p[0] + diff_x * k, p[1] + diff_y * k)
            k += 1

        k = 0
        antinode_pos_2 = (q[0] - diff_x * k, q[1] - diff_y * k)
        while antinode_pos_2 in idx_pairs:
            antinodes_rec_part2.add(antinode_pos_2)
            antinode_pos_2 = (q[0] - diff_x * k, q[1] - diff_y * k)
            k += 1

part1 = len(antinodes_rec_part1)
part2 = len(antinodes_rec_part2)
print(part1, part2)
