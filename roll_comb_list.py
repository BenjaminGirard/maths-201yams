#!/usr/bin/env python
## roll_comb_list.py for roll_comb_list in /home/renaud/Documents/Tech2/Py/Maths/201yams
## 
## Made by Renaud de Ganay
## Login   <renaud@epitech.net>
## 
## Started on  Mon Feb 13 14:20:01 2017 Renaud de Ganay
## Last update Mon Feb 13 17:42:35 2017 benjamin girard
##

def roll_comb(dices):
    init_list = [[1] * dices]
    curr_list = [1] * dices
    while curr_list != [6] * dices:
        off = 0
        if curr_list[0] < 6:
            curr_list[0] += 1
        else:
            while curr_list[off] == 6:
                curr_list[off] = 1
                off += 1
            curr_list[off] += 1
        init_list.append(list(curr_list))
    return init_list
