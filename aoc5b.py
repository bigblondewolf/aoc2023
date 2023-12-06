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


def do_reverse_map(src, dst, value):
    for i, dst_start in enumerate(MAPS[src+"-"+dst]["dst_start"]):
        if dst_start <= value and value <= MAPS[src+"-"+dst]["dst_start"][i] + MAPS[src+"-"+dst]["range"][i] + 1:
            return(MAPS[src+"-"+dst]["src_start"][i] + value  - dst_start)
    return(value)


def find_map(src):
    for this_map in MAPS:
        if this_map.startswith(src):
            return(this_map)
    return None


def find_map_by_dst(dst):
    for this_map in MAPS:
        if this_map.endswith(dst):
            return(this_map)
    return None

def find_next_map(a_map):
    map_src, map_dst = re.search("([a-z]+)-([a-z]+)", a_map).groups()
    for this_map in MAPS:
        if this_map.startswith(map_dst):
            return(this_map)
    return None


def find_prev_map(a_map):
    map_src, map_dst = re.search("([a-z]+)-([a-z]+)", a_map).groups()
    for this_map in MAPS:
        if this_map.endswith(map_src):
            return(this_map)
    return None


def map_src_dst(a_map):
    return a_map.split("-")


def seed_is_in_range(seed):
    #print("seed: {}".format(seed))
    for i in range(0, int(len(BIG_MAP["seed"])/2), 2):
        #print("Range: {} {}".format(BIG_MAP["seed"][i], BIG_MAP["seed"][i] +
        #                            BIG_MAP["seed"][i+1]))
        if seed >= BIG_MAP["seed"][i] and seed <= BIG_MAP["seed"][i] + BIG_MAP["seed"][i+1]:
            return True
    return False


def indent_print(indent, txt):
    print("{}{}".format(" " * indent, txt))


def minmax_in_one_map_entry(indent, src, vmin, vmax):
    """Checks if the range min-max of src appears only within one line in
    src-dst map."""
    a_map = MAPS[find_map(src)]
    indent_print(indent, "--- Reading map for {} ---".format(src))
    for i in range(len(a_map["src_start"])):
        indent_print(indent, "--- Range {} start ---".format(src))
        if vmin >= a_map["src_start"][i] and vmin <= a_map["src_start"][i] + a_map["range"][i]:
            indent_print(indent, "{} vmin {} within range {} {}".format(src, vmin,
                                                         a_map["src_start"][i],
                                                         a_map["src_start"][i]
                                                         + a_map["range"][i]))
        if vmax >= a_map["src_start"][i] and vmax <= a_map["src_start"][i] + a_map["range"][i]:
            indent_print(indent, "{} vmax {} within range {} {}".format(src, vmin,
                                                         a_map["src_start"][i],
                                                         a_map["src_start"][i]
                                                         + a_map["range"][i]))
        if a_map["src_start"][i] > a_map["dst_start"][i]:
            indent_print(indent, "{} src_start {} remaps backwards".format(src, a_map["src_start"][i]))
        indent_print(indent, "--- Range {} end ---".format(src))


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
#fill_big_map()

## Forward mapping
#this_map = find_map("seed")
#src_val = 3955612581
#while this_map:
#    src, dst = map_src_dst(this_map)
#    dst_val = do_map(src, dst, src_val)
#    print("{} {} {} {}".format(src, src_val, dst, dst_val))
#    src_val = dst_val
#    this_map = find_next_map(this_map)
#
# Reverse mapping
#this_map = find_map_by_dst("location")
#dst_val = 0
#while this_map:
#    src, dst = map_src_dst(this_map)
#    src_val = do_reverse_map(src, dst, dst_val)
#    #print("{} {} {} {}".format(src, src_val, dst, dst_val))
#    dst_val = src_val
#    this_map = find_prev_map(this_map)

# Brute force reverse mapping
max_iters = 400000000
loc_val =   350000000
while True:
    if loc_val> max_iters:
        raise RecursionError("{} operations".format(loc_val))
    dst_val = loc_val
    this_map = find_map_by_dst("location")
    while this_map:
        src, dst = map_src_dst(this_map)
        src_val = do_reverse_map(src, dst, dst_val)
        #print("{} {} {} {}".format(src, src_val, dst, dst_val))
        dst_val = src_val
        this_map = find_prev_map(this_map)
    if seed_is_in_range(src_val):
        raise Exception("Found seed {}, location {}".format(src_val, loc_val))
    if loc_val % 10000 == 0:
        print(loc_val)
    loc_val += 1




#for i in range(0, int(len(BIG_MAP["seed"])/2), 2):
#    print(i)
#    vmin = BIG_MAP["seed"][i]
#    vmax = BIG_MAP["seed"][i+2]
#    this_map = find_map("seed")
#    indent = 0
#    while this_map:
#        src, dst = map_src_dst(this_map)
#        minmax_in_one_map_entry(indent, src, vmin, vmax)
#        src_min = do_map(src, dst, vmin)
#        src_max = do_map(src, dst, vmax)
#        this_map = find_next_map(this_map)
#        indent += 2


