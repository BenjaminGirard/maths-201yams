#!/usr/bin/env python3.4
## interface.py for  in /home/renaud/Documents/Tech2/Py/Maths/201yams/bonus
##
## Made by Renaud de Ganay
## Login   <renaud@epitech.net>
##
## Started on  Mon Feb 13 23:35:00 2017 Renaud de Ganay
## Last update Wed Feb 15 11:23:09 2017 benjamin girard
##

import math

from appJar import gui

from launch_form import launch_form
from app import app
from app import opt_list
from proba import find_wanted_proba

dice_status = {
    "dice1": 0,
    "dice2": 0,
    "dice3": 0,
    "dice4": 0,
    "dice5": 0,
}

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

def changePic(btn):
    dice_status[btn] = dice_status[btn] + 1 if dice_status[btn] < 6 else 0
    app.setImage(str(btn), "dices_pictures/dice{nb}.gif".format(nb=dice_status[btn]))

def launch_dices():
    app.addImage("dice1", "dices_pictures/dice0.gif", 1, 4)
    app.addImage("dice2", "dices_pictures/dice0.gif", 1, 5)
    app.addImage("dice3", "dices_pictures/dice0.gif", 1, 6)
    app.addImage("dice4", "dices_pictures/dice0.gif", 1, 7)
    app.addImage("dice5", "dices_pictures/dice0.gif", 1, 8)
    app.setImageFunction("dice1", changePic)
    app.setImageFunction("dice2", changePic)
    app.setImageFunction("dice3", changePic)
    app.setImageFunction("dice4", changePic)
    app.setImageFunction("dice5", changePic)

def launch_meter(proba, title, name):
    colors = {
        0: "#E50017",
        10: "#E11F00",
        20: "#DD5300",
        30: "#D98600",
        40: "#D5B700",
        50: "#BDD200",
        60: "#88CE00",
        70: "#55CA00",
        80: "#24C600",
        90: "#00C20A",
        100: "#00BF38"
    }
    app.setMeter(title, proba, "{name}: {proba} %".format(name=name, proba=proba))
    app.setMeterFill(title, colors[roundup(int(proba))])
    app.showMeter(title)

def get_comb_list_from_user():
    for opt, state in opt_list.items():
        if state == True:
            box = opt
            break
    if "ValueFull" not in box:
        user_comb_list = [app.getOptionBox("Combination").lower(), app.getOptionBox(box)]
    else:
        user_comb_list = ["full", app.getOptionBox("ValueFull1"), app.getOptionBox("ValueFull2")]
    return user_comb_list


def press_compute(btn):
    dice_list = [list[1] for list in dice_status.items()]
    user_comb_list = get_comb_list_from_user()
    proba = find_wanted_proba(dice_list, user_comb_list)
    proba = round((proba * 100), 2)
    launch_meter(proba, "Probability", "Probability")
    app.showMessage("result")
    app.addHorizontalSeparator(6, 1, 6, colour="green")
    app.showMessage("list_result")
    full_value = user_comb_list[1] if len(user_comb_list) < 3 else user_comb_list[2]
    pb_list = [
        (find_wanted_proba(dice_list, ["pair", user_comb_list[1]]), "pair"),
        (find_wanted_proba(dice_list, ["three", user_comb_list[1]]), "three"),
        (find_wanted_proba(dice_list, ["four", user_comb_list[1]]), "four"),
        (find_wanted_proba(dice_list, ["full", user_comb_list[1], full_value]), "full"),
        (find_wanted_proba(dice_list, ["straight", user_comb_list[1]]), "straight"),
        (find_wanted_proba(dice_list, ["yams", user_comb_list[1]]), "yams"),
    ]
    pb_list.sort(key=lambda x: x[0])
    for i, plist in enumerate(pb_list):
        launch_meter(round(plist[0] * 100, 2), "pb{n}".format(n=(i+1)), plist[1])

def compute_form_button():
    app.addButton("Compute", press_compute, 2, 3)
    app.hideButton("Compute")

def set_hide():
    app.addMeter("Probability", 5, 1, 6)
    app.hideMeter("Probability")
    app.addMessage("result", "Your result:", 4, 1, 6)
    app.hideMessage("result")
    app.addMessage("list_result", "list of potential results:", 7, 1, 6)
    app.hideMessage("list_result")
    app.addMeter("pb1", 8, 1, 6)
    app.hideMeter("pb1")
    app.addMeter("pb2", 9, 1, 6)
    app.hideMeter("pb2")
    app.addMeter("pb3", 10, 1, 6)
    app.hideMeter("pb3")
    app.addMeter("pb4", 11, 1, 6)
    app.hideMeter("pb4")
    app.addMeter("pb5", 12, 1, 6)
    app.hideMeter("pb5")
    app.addMeter("pb6", 13, 1, 6)
    app.hideMeter("pb6")


def launch_interface():
    app.setFont(19)
    app.setBg("#d9dbdd")
    set_hide()
    launch_dices()
    launch_form(app)
    compute_form_button()
    app.go()
