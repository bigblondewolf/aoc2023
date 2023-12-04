#!/usr/bin/env python

INFN = "aoc4.txt"

with open(INFN) as INF:
    lines = INF.readlines()

cards = {"winning": [[]], "elf": [[]], "repetitions": [0]}

for l in lines:
    ll = l.split(": ")[1].strip().replace("  ", " ").split(" | ")
    cards["winning"].append(ll[0].split(" "))
    cards["elf"].append(ll[1].split(" "))
    cards["repetitions"].append(1)

for i, (w, e) in enumerate(zip(cards["winning"], cards["elf"])):
    if i == 0:
        # Skip zeroth card, it is there for convenience.
        continue
    for this_card_rep in range(cards["repetitions"][i]):
        wins = 0
        for n in e:
            if n in w:
                wins += 1
        if wins > 0:
            for win_nr in range(wins):
                if i + win_nr + 1 <= len(cards["repetitions"]):
                    cards["repetitions"][i+win_nr+1] += 1
print(sum(cards["repetitions"]))
