#!/usr/bin/env python3

import re

INFN = "aoc3.txt"


def is_symbol(char):
    return char == "*"
    #return char not in "0123456789.\n"


def lexp(line):
    """Prepend a line with a dot.

    Helps processing when a match is found at the beginning of the line.
    The last char is always \n."""
    return "." + line


with open(INFN) as INF:
    lines = INF.readlines()
num = re.compile("[0-9]+")
numend = re.compile("[0-9]+$")
numstart = re.compile("^[0-9]+")
sum_ratios = 0
for ln,l in enumerate(lines):
    le = lexp(l)
    for sn, sym in enumerate(le):
        if not is_symbol(sym):
            continue
        adjacent_nums = []
        # Check for numbers left to the symbol.
        numsleft = numend.search(le[:sn])
        if numsleft:
            adjacent_nums.append(numsleft.group())
        # Check for numbers right to the symbol.
        numsright = numstart.search(le[sn+1:])
        if numsright:
            adjacent_nums.append(numsright.group())
        # Check for numbers above the symbol.
        if ln > 0:
            ple = lexp(lines[ln-1])
            for n in num.finditer(ple):
                if n.span()[0] < sn + 2 and n.span()[1] >= sn:
                    adjacent_nums.append(n.group())
        # Check for numbers below the symbol.
        if ln < len(lines)-1:
            nle = lexp(lines[ln+1])
            for n in num.finditer(nle):
                if n.span()[0] < sn + 2 and n.span()[1] >= sn:
                    adjacent_nums.append(n.group())
        if len(adjacent_nums) == 2:
            sum_ratios += int(adjacent_nums[0]) * int(adjacent_nums[1])
print(sum_ratios)
