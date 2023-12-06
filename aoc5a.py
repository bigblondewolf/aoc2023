#!/usr/bin/env python3

import re
import pandas as pd

INFN = "aoc5.txt"
#INFN = "aoc5_example.txt"

MAPS = {}
BIG_MAP = {}


def do_map(src, dst, value):
    for i, src_start in enumerate(MAPS[src+"-"+dst]["src_start"]):
        if src_start <= value and value <= MAPS[src+"-"+dst]["src_start"][i] + MAPS[src+"-"+dst]["range"][i] + 1:
            return(MAPS[src+"-"+dst]["dst_start"][i] + value  - src_start)
    return(value)


def find_map(src):
    for this_map in MAPS:
        if this_map.startswith(src):
            return(this_map)
    return None


def find_next_map(a_map):
    map_src, map_dst = re.search("([a-z]+)-([a-z]+)", a_map).groups()
    for this_map in MAPS:
        if this_map.startswith(map_dst):
            return(this_map)
    return None


def map_src_dst(a_map):
    return a_map.split("-")


def fill_big_map():
    for seed in BIG_MAP["seed"]:
        this_map = find_map("seed")
        src_val = seed
        while this_map:
            src, dst = map_src_dst(this_map)
            dst_val = do_map(src, dst, src_val)
            BIG_MAP[dst].append(dst_val)
            src_val = dst_val
            this_map = find_next_map(this_map)


with open(INFN) as INF:
    in_map = None
    for l in INF.readlines():
        if l.strip() == "":
            in_map = None
            continue
        if l.startswith("seeds:"):
            BIG_MAP["seed"] = [int(x) for x in l.split(": ")[1].split(" ")]
            continue
        if l.endswith("map:\n"):
            mapre = re.compile("([a-z]+)-to-([a-z]+) map:")
            in_map = mapre.search(l).groups()[0] + "-" + mapre.match(l).groups()[1]
            MAPS[in_map] = {"src_start": [], "dst_start": [], "range": []}
            BIG_MAP[mapre.match(l).groups()[1]] = []
            continue
        ll = l.strip().split()
        MAPS[in_map]["dst_start"].append(int(ll[0]))
        MAPS[in_map]["src_start"].append(int(ll[1]))
        MAPS[in_map]["range"].append(int(ll[2]))
fill_big_map()
print(do_map("soil", "fertilizer", 81))
df_small_map = pd.DataFrame(MAPS)
df_big_map = pd.DataFrame(BIG_MAP)
print(df_small_map)
print(df_big_map)
print(min(BIG_MAP["location"]))
