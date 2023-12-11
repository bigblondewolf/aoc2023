#!/usr/bin/env python3

import itertools

INFN = "aoc11.txt"


EXPANSION_OFFSET = 1000000

def remap_galaxy(galaxy, rows_empty, cols_empty):
    x = galaxy[0]
    y = galaxy[1]
    xnew = x
    ynew = y
    for r in rows_empty:
        if r < x:
            xnew += (EXPANSION_OFFSET - 1)
    for c in cols_empty:
        if c < y:
            ynew += (EXPANSION_OFFSET - 1)
    return(xnew, ynew)


def calc_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return(abs(x1-x2)+abs(y1-y2))


#Read in from file
with open(INFN) as INF:
    rows_non_empty = []
    cols_non_empty = []
    image = []
    galaxies = []
    for ln, l in enumerate(INF.readlines()):
        image.append(l.strip())
        if "#" in l:
            rows_non_empty.append(ln)
            for cn, col in enumerate(l.strip()):
                if col == "#":
                    cols_non_empty.append(cn)
rows_empty = [r for r in range(len(image)) if r not in rows_non_empty]
cols_empty = [c for c in range(len(image[0])) if c not in cols_non_empty]

galaxies = []
for rn, r in enumerate(image):
    for cn, c in enumerate(r):
        if c == "#":
            galaxies.append(remap_galaxy((rn, cn), rows_empty, cols_empty))

sum_paths = 0
combos = itertools.combinations(galaxies, 2)
print("Got {} combos from {} galaxies.".format(len([c for c in combos]), len(galaxies)))
for cn, combo in enumerate(itertools.combinations(galaxies, 2)):
    sum_paths += calc_dist(*combo)
print(sum_paths)

