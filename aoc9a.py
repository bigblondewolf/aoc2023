#!/usr/bin/env python3

#INFN = "aoc9_example.txt"
INFN = "aoc9.txt"

with open(INFN) as INF:
    lines = INF.readlines()

total_sum = 0
for lraw in lines:
    print()
    print()
    print()
    l = [[int(x) for x in lraw.strip().split()]]
    all_zeroes = False
    iter = 1
    while not all_zeroes:
        print(l)
        nl = []
        all_zeroes = True
        print(iter)
        for i, v in enumerate(l[iter-1]):
            if i == len(l[iter-1]) - 1:
                continue
            diff = l[iter-1][i+1] - l[iter-1][i]
            if diff != 0:
                all_zeroes = False
            nl.append(diff)
        l.append(nl)
        iter += 1
    for ln in range(len(l), 0, -1):
        l[ln-2].append(l[ln-1][-1] + l[ln-2][-1])
    total_sum += l[0][-1]
print(total_sum)


