#!/usr/bin/env python3

import networkx as nx

INFN = "aoc10.txt"
#INFN = "aoc10_example.txt"


with open(INFN) as INF:
    lines = INF.readlines()

G = nx.Graph()

w = len(lines[0])
h = len(lines)
for r, row in enumerate(lines):
    for c, char in enumerate(row):
        if char == "|":
            if r > 0 and lines[r-1][c] in "7F|":
                G.add_edge((r, c), (r-1, c))
            if r < h-2 and lines[r+1][c] in "JL|":
                G.add_edge((r, c), (r+1, c))
        if char == "-":
            if c > 0 and row[c-1] in "LF-":
                G.add_edge((r, c), (r, c-1))
            if r < w-2 and row[c+1] in "J7-":
                G.add_edge((r, c), (r, c+1))
        if char == "L":
            if r > 0 and lines[r-1][c] in "7F|":
                G.add_edge((r, c), (r-1, c))
            if c < w-2 and row[c+1] in "7J-":
                G.add_edge((r, c), (r, c+1))
        if char == "J":
            if r > 0 and lines[r-1][c] in "7F|":
                G.add_edge((r, c), (r-1, c))
            if c > 0 and row[c-1] in "LF-":
                G.add_edge((r, c), (r, c-1))
        if char == "7":
            if r < h-2 and lines[r+1][c] in "JL|":
                G.add_edge((r, c), (r+1, c))
            if c > 0 and row[c-1] in "LF-":
                G.add_edge((r, c), (r, c-1))
        if char == "F":
            if r < h-2 and lines[r+1][c] in "JL|":
                G.add_edge((r, c), (r+1, c))
            if c < h-2 and row[c+1] in "7J-":
                G.add_edge((r, c), (r, c+1))
# S is 42,8 in input data
print( (nx.shortest_path_length(G, (42,9), (43,8)) / 2) + 1)
