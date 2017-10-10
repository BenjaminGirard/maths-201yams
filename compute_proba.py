#!/usr/bin/env python
## compute_proba.py for  in /home/tetard/EPITECH_Y2/maths/201yams
##
## Made by benjamin girard
## Login   <tetard@epitech.net>
##
## Started on  Mon Feb 13 14:35:21 2017 benjamin girard
## Last update Wed Feb 15 10:18:25 2017 benjamin girard
##

from collections import Counter
from roll_comb_list import roll_comb

def compute_pair_proba(dice_list, comb_list):
    count = dice_list.count(int(comb_list[1]))
    if count >= 2:
        return 1
    combs = roll_comb(5 - count)
    res= 0
    for comb in combs:
        if comb.count(int(comb_list[1])) >= (2 - count):
            res += 1
    return float(res) / len(combs)

def compute_three_proba(dice_list, comb_list):
    count = dice_list.count(int(comb_list[1]))
    if count >= 3:
        return 1
    combs = roll_comb(5 - count)
    res= 0
    for comb in combs:
        if comb.count(int(comb_list[1])) >= (3 - count):
            res += 1
    return float(res) / len(combs)

def compute_four_proba(dice_list, comb_list):
    count = dice_list.count(int(comb_list[1]))
    if count >= 4:
        return 1
    combs = roll_comb(5 - count)
    res= 0
    for comb in combs:
        if comb.count(int(comb_list[1])) >= (4 - count):
            res += 1
    return float(res) / len(combs)

def compute_yams_proba(dice_list, comb_list):
    finder = int(comb_list[1])
    count = dice_list.count(int((comb_list[1])))
    if count == 5:
        return 1
    res = 0
    combs = roll_comb(5 - count)
    for comb in combs:
        if comb.count(int(comb_list[1])) >= (5 - count):
            res += 1
    return float(res) / len(combs)

def compute_full_proba(dice_list, comb_list):
    if (int(comb_list[1]) == int(comb_list[2])):
        return compute_yams_proba(dice_list, comb_list)
    major = dice_list.count(int(comb_list[1]))
    minor = dice_list.count(int(comb_list[2]))
    if major == 3 and minor == 2:
        return 1
    list_to_find = [int(comb_list[1])] * (3 - major)
    list_to_find += [int(comb_list[2])] * (2 - minor)
    combs = roll_comb(len(list_to_find))
    res = 0
    for comb in combs:
        if sorted(list_to_find) == sorted(comb):
            res += 1
    return float(res) / len(combs)

def compute_straight_proba(dice_list, comb_list):
    index = 2 if int(comb_list[1]) == 6 else 1
    list_to_find = []
    count = 0
    for i in range(0, 5):
        if index in dice_list:
            count += 1
        else:
            list_to_find.append(index)
        index += 1;
    combs = roll_comb(5 - count)
    res = 0
    for comb in combs:
        if set(list_to_find) <= set(comb):
            res += 1
    return float(res) / len(combs)
