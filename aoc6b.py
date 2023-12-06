#!/usr/bin/env python3

import math

#INFN = "aoc6_example.txt"
INFN = "aoc6.txt"

CR = 1   # accelleration 1mm/ms for each second charging.

# S -CR*tc^2 + CR*ttot*tc
# Where
# S is the distance traveled
# CR is the charging rate
# tc is time charging
# ttot is the total time (from the input data)


TIMES = []
DISTANCES = []
with open(INFN) as INF:
    for l in INF.readlines():
        if l.startswith("Time:"):
            TIMES = [int(l.strip().replace(" ", "").split(":")[1])]
        if l.startswith("Distance:"):
            DISTANCES = [int(l.strip().replace(" ", "").split(":")[1])]

print(TIMES)
print(DISTANCES)

total_product = 1
for ttot, dist in zip(TIMES, DISTANCES):
    tcmax = (CR * ttot) / (2 * CR)
    tcmin1 = ((CR * ttot) + math.sqrt( pow(CR*ttot, 2) - 4 * CR * dist)) / (2 * CR)
    tcmin2 = ((CR * ttot) - math.sqrt( pow(CR*ttot, 2) - 4 * CR * dist)) / (2 * CR)
    print("tcmin1: {} tcmax: {} tcmin2: {}".format(tcmin1, tcmax, tcmin2))
    tcmin_low = min(tcmin1, tcmin2)
    tcmin_hi = max(tcmin1, tcmin2)
    if tcmin_low.is_integer():
        tcmin_low += 1
    #if tcmin_low.is_integer():
    #    tcmin_hi -= 1
    tcmin_low = math.floor(tcmin_low) + 1
    tcmin_hi = math.floor(tcmin_hi)
    nums = range(tcmin_low, tcmin_hi)
    print(nums)
    print(len(nums)+1)
    total_product *= len(nums) + 1
print(total_product)
