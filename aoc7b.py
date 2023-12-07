#!/usr/bin/env python3

import functools
import re

INFN = "aoc7.txt"
#INFN = "aoc7_example.txt"

CARD_RANKS = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
HAND_RANKS = ["HC", "P1", "P2", "K3", "FH", "K4", "K5"]

def rank_hand(hand):
    # Use sets for most common hands 1p and hc
    # If different ranks produce same set length, check with a regexp.
    set_len = len(set(hand))
    if set_len == 5:
        return("HC")
    if set_len == 4:
        # One pair.
        return("P1")
    if set_len == 3:
        # Three of a kind or two pair.
        hand_sorted = "".join(sorted(hand))
        if re.search(r"([a-zA-Z0-9])\1\1", hand_sorted):
            return("K3")
        return("P2")
    if set_len == 2:
        # Four of a kind or full house.
        hand_sorted = "".join(sorted(hand))
        if re.search(r"([a-zA-Z0-9])\1\1\1", hand_sorted):
            return("K4")
        return("FH")
    if set_len == 1:
        # Five of a kind.
        return("K5")
    raise ValueError("Hand '{}' doesn't fit spec!".format(hand))


def rank_hand_with_joker(hand):
    if "J" not in hand:
        return(rank_hand(hand))
    max_rank = "HC"
    for card in CARD_RANKS:
        hand_new = ""
        for c in hand:
            if c == "J":
                hand_new += card
            else:
                hand_new += c
        if HAND_RANKS.index(rank_hand(hand_new)) > HAND_RANKS.index(max_rank):
            print("!")
            max_rank = rank_hand(hand_new)
    return(max_rank)


def cmp_hands(lh, rh):
    lhr = HAND_RANKS.index(rank_hand_with_joker(lh))
    rhr = HAND_RANKS.index(rank_hand_with_joker(rh))
    if lhr < rhr:
        return(-1)
    if lhr > rhr:
        return(1)
    for i in range(len(lh)):
        if CARD_RANKS.index(lh[i]) < CARD_RANKS.index(rh[i]):
            return(-1)
        if CARD_RANKS.index(lh[i]) > CARD_RANKS.index(rh[i]):
            return(1)
    return(0)


HANDS = {}
with open(INFN) as INF:
    wins = 0
    for l in INF.readlines():
        line_l = l.split()
        HANDS[line_l[0]] = int(line_l[1])
    HANDS_RANKED = sorted(HANDS.keys(), key=functools.cmp_to_key(cmp_hands))
    for i, h in enumerate(HANDS_RANKED):
        wins += (i+1) * HANDS[h]
    print(wins)
