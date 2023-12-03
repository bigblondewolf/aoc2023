#!/usr/bin/env python3

import re

INFN = "aoc3.txt"


def is_symbol(char):
    return char not in "0123456789.\n"


def lexp(line):
    """Prepend a line with a dot.

    Helps processing when a match is found at the beginning of the line.
    The last char is always \n."""
    return "." + line


with open(INFN) as INF:
    lines = INF.readlines()
num = re.compile("[0-9]+")
numend = re.compile("[0-9]+$")
numstart = re.compile("^\[0-9]+")
sum_ratios = 0
for ln,l in enumerate(lines):
    le = lexp(l)
    for sn, sym in enumerate(le):
        try:
            if not is_symbol(sym):
                continue
            print()
            adjacent_nums = []
            # Check for numbers left to the symbol.
            numsleft = numend.search(le[:sn])
            if numsleft:
                adjacent_nums.append(numsleft.group())
                print("an1: {}".format(adjacent_nums))
            # Check for numbers right to the symbol.
            numsright = numstart.search(le[sn+1:])
            if numsright:
                adjacent_nums.append(numsright.group())
                print("an2: {}".format(adjacent_nums))
            # Check for numbers above the symbol.
            if ln > 0:
                ple = lexp(lines[ln-1])
                for n in num.finditer(ple):
                    if n.span()[0] <= sn + 1 and n.span()[1] >= sn - 1:
                        adjacent_nums.append(n.group())
                        print("an3: {}".format(adjacent_nums))
            # Check for numbers below the symbol.
            if ln < len(lines)-1:
                nle = lexp(lines[ln+1])
                for n in num.finditer(nle):
                    if n.span()[0] <= sn + 1 and n.span()[1] >= sn - 1:
                        adjacent_nums.append(n.group())
                        print("an4: {}".format(adjacent_nums))
            print("{} {}".format(ln-1, ple.strip()))
            print("{} {}".format(ln, le.strip()))
            print("{} {}".format(ln+1, nle.strip()))
            print("{} {}".format(sn, sym))
            if numsleft:
                print("nums to the left: {}".format(numsleft))
                print("nums to the left: {}".format(numsleft.group()))
                print("string: " + le[:sn])
            if numsright:
                print("nums to the right: {}".format(numsright))
                print("string: " + le[sn+1:])
            print("Adjacent nums: {}".format(adjacent_nums))
            if len(adjacent_nums) == 2:
                sum_ratios += int(adjacent_nums[0]) * int(adjacent_nums[1])
        except Exception as e:
            print("{} {}".format(ln-1, lle.strip()))
            print("{} {}".format(ln, le.strip()))
            print("{} {}".format(ln+1, nle.strip()))
            print("{} {}".format(sn, sym))
            print("nums to the left: {}".format(numsleft))
            print("nums to the right: {}".format(numsright))
            raise e
print(sum_ratios)
