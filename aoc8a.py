#!/usr/bin/env python3

#INFN = "aoc8_example.txt"
INFN = "aoc8.txt"

MAP = {}
DIRECTIONS = []

with open(INFN) as INF:
    for ln, l in enumerate(INF.readlines()):
        if ln == 0:
            for x in l.strip():
                if x == "L":
                    DIRECTIONS.append(0)
                if x == "R":
                    DIRECTIONS.append(1)
            continue
        if ln == 1:
            continue
        mk = l.split(" = ")[0]
        mv = l.strip().split(" = ")[1][1:-1].split(", ")
        MAP[mk] = mv


START = "AAA"
END = "ZZZ"

for node in MAP:
    if node == START:
        next_step = MAP[node][DIRECTIONS[1]]
        print("{} {} {}".format(node, DIRECTIONS[0], next_step))
        step_nr = 1
        while next_step != END:
            nn = step_nr%len(DIRECTIONS)
            print()
            print("{} {}".format(step_nr, nn))
            next_step = MAP[next_step][DIRECTIONS[nn]]
            print("{} {} {}".format(node, DIRECTIONS[nn], next_step))
            step_nr += 1
print(step_nr)
