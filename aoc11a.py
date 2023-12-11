#!/usr/bin/env python3

import networkx as nx
import itertools

#INFN = "aoc11_example1.txt"
INFN = "aoc11.txt"

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
print("Read image.")

# Expand image
row_add_offset = 0
for r in rows_empty:
    image.insert(r+row_add_offset, "."*len(image[r]))
    row_add_offset += 1
col_add_offset = 0
for c in cols_empty:
    for rn, r in enumerate(image):
        image[rn] = r[:c+col_add_offset] + "." + r[c+col_add_offset:]
    col_add_offset += 1
print("Expanded image.")

#Fill graph and find galaxies
G = nx.Graph()
galaxies = []
for rn, r in enumerate(image):
    for cn, c in enumerate(r):
        if c == "#":
            galaxies.append((rn, cn))
        if rn > 0:
            G.add_edge((rn, cn), (rn-1, cn))
        if rn < len(image) - 1:
            G.add_edge((rn, cn), (rn+1, cn))
        if cn > 0:
            G.add_edge((rn, cn), (rn, cn-1))
        if cn < len(r) - 1:
            G.add_edge((rn, cn), (rn, cn+1))
print("Generated graph.")
sum_paths = 0
combos = itertools.combinations(galaxies, 2)
print("Got {} combos from {} galaxies.".format(len([c for c in combos]), len(galaxies)))
for cn, combo in enumerate(itertools.combinations(galaxies, 2)):
    sum_paths += nx.shortest_path_length(G, combo[0], combo[1])
    if cn % 100 == 0:
        print("Combo {}".format(cn))
print(sum_paths)

