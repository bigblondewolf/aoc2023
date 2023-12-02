#!/usr/bin/env python3

CUBES = {"r": 12, "g": 13, "b": 14}

INFN = "aoc2a.txt"

with open(INFN) as INF:
    sum_possible_games = 0
    for ln, l in enumerate(INF.readlines()):
        game_rounds = l.replace("; ", ";").replace(", ", ",").split(": ")[1].split(";")
        print(game_rounds)
        game_possible = True
        for gr in game_rounds:
            gr_d = {"red": 0, "green": 0, "blue": 0}
            for col_r in gr.strip().split(","):
                gr_d[col_r.split(" ")[1]] = int(col_r.split(" ")[0])
                if gr_d["red"] > CUBES["r"] or gr_d["green"] > CUBES["g"] or gr_d["blue"] > CUBES["b"]:
                    game_possible = False
        if game_possible:
            sum_possible_games += ln + 1
        print("{} {} {}".format(ln + 1, game_possible, l))
print(sum_possible_games)

