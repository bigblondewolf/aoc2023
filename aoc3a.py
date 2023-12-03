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


def contains_sym(line_slice):
    """Returns true if the slice of a line (string) contains a symbol."""
    for char in line_slice:
        if is_symbol(char):
            return(True)
    return(False)


with open(INFN) as INF:
    lines = INF.readlines()

nums = re.compile("[0-9]+")
sum_pn = 0 
for ln, l in enumerate(lines):
    for m in nums.finditer(l):
        try:
            span_min = m.span()[0]
            span_max = m.span()[1]
            le = lexp(l)
            # Search adjacent symbol on current line first
            if is_symbol(le[span_min]) or is_symbol(le[span_max+1]):
                    sum_pn += int(m.group())
                    continue
            if ln > 0:
                # Check previous lines only after line 1.
                le = lexp(lines[ln-1])
                if contains_sym(le[span_min:span_max+2]):
                    sum_pn += int(m.group())
            if ln < len(lines)-1:
                # Check next line only until last but one line.
                le = lexp(lines[ln+1])
                if contains_sym(le[span_min:span_max+2]):
                    sum_pn += int(m.group())
        except Exception as e:
            print(ln)
            print("'{}'".format(l))
            print("'{}'".format(le))
            print("Lenght: {}".format(len(l)))
            print("Lenght: {}".format(len(le)))
            print(m)
            print("'{}'".format(le[span_max+2]))
            raise e
print(sum_pn)




