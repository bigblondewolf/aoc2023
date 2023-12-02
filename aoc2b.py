#!/usr/bin/env python3

INFN = "aoc2a.txt"

with open(INFN) as INF:
    sum_powers = 0
    for ln, l in enumerate(INF.readlines()):
        game_rounds = l.replace("; ", ";").replace(", ", ",").split(": ")[1].split(";")
        min_r = 0
        min_g = 0
        min_b = 0
        for gr in game_rounds:
            for color_result in gr.strip().split(","):
                if color_result.split(" ")[1] == "red":
                    if int(color_result.split(" ")[0]) > min_r:
                        min_r = int(color_result.split(" ")[0])
                if color_result.split(" ")[1] == "green":
                    if int(color_result.split(" ")[0]) > min_g:
                        min_g = int(color_result.split(" ")[0])
                if color_result.split(" ")[1] == "blue":
                    if int(color_result.split(" ")[0]) > min_b:
                        min_b = int(color_result.split(" ")[0])
            print("{} {} {} {} {}".format(min_r * min_g * min_b, min_r, min_g, min_b, l))
        sum_powers += min_r * min_g * min_b
print(sum_powers)

