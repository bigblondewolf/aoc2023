#!/usr/bin/env python3

import networkx as nx
from shapely.geometry import Point, Polygon

INFN = "aoc10.txt"

with open(INFN) as INF:
    lines = [l.strip() for l in INF.readlines()]

G = nx.Graph()

w = len(lines[0])
h = len(lines)
print("w {} h {}".format(w, h))
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
            if c < w-2 and row[c+1] in "J7-":
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
        if char == "S":
            print("S: {} {}".format(r, c))
            START = (r, c)
# Starting point in my dataset is 42, 8
shortest_path = nx.shortest_path(G, (42, 9), (43, 8))
shortest_path.append(START)

poly = Polygon(shortest_path)
points_in = 0
for r in range(h):
    for c in range(w):
        p = Point(r, c)
        if poly.contains(p):
            points_in += 1
print(points_in)
