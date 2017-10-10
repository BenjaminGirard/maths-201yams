#!/usr/bin/env python3.3
# graphics.py for  in /home/renaud/Documents/Tech2/Py/Maths/201yams/bonus
## 
## Made by Renaud de Ganay
## Login   <renaud@epitech.net>
## 
## Started on  Mon Feb 13 18:13:40 2017 Renaud de Ganay
## Last update Mon Feb 13 23:36:35 2017 Renaud de Ganay
##

from appJar import gui

from app import app
from app import opt_list

def hide_all_opt():
    for opt, state in opt_list.items():
        app.hideOptionBox(opt)
        opt_list[opt] = False

def press_comb(btn):
    box_val = app.getOptionBox("Combination")
    if box_val in ("pair", "three", "four", "yams"):
        hide_all_opt()
        app.showOptionBox("ValueSimple")
        opt_list["ValueSimple"] = True
    elif box_val in ("straight"):
        hide_all_opt()
        app.showOptionBox("ValueStraight")
        opt_list["ValueStraight"] = True
    elif box_val in ("full"):
        hide_all_opt()
        app.showOptionBox("ValueFull1")
        app.showOptionBox("ValueFull2")
        opt_list["ValueFull1"] = True
        opt_list["ValueFull2"] = True
    app.showButton("Compute")


def launch_form(app):
    app.addLabelOptionBox("Combination", ["pair", "three", "four", "straight", "full", "yams"], 1, 0)
    app.addButton("Validate Combination", press_comb, 1, 1)

    app.addOptionBox("ValueSimple", ["1", "2", "3", "4", "5", "6",], 1, 2)
    app.addOptionBox("ValueStraight", ["5", "6",], 1, 2)
    app.addOptionBox("ValueFull1", ["1", "2", "3", "4", "5", "6",], 1, 2)
    app.addOptionBox("ValueFull2", ["1", "2", "3", "4", "5", "6",], 1, 3)
    hide_all_opt()
