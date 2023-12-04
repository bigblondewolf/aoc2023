#!/usr/bin/env python

INFN = "aoc4.txt"

with open(INFN) as INF:
    lines = INF.readlines()

cards = {"winning": [[]], "elf": [[]]}

for l in lines:
    ll = l.split(": ")[1].strip().replace("  ", " ").split(" | ")
    cards["winning"].append(ll[0].split(" "))
    cards["elf"].append(ll[1].split(" "))

score = 0
for w, e in zip(cards["winning"], cards["elf"]):
    this_score = 0
    nums_winning = []
    for n in e:
        if n in w:
            nums_winning.append(n)
            if this_score == 0:
                this_score = 1
                continue
            this_score = this_score * 2
    score += this_score
print(score)