#!/usr/bin/env python

from xdice import * 

primary_roll  = roll("1d100")

phb_race_table = (
	{"RACE":"Dragonborn","LOW":1,"HIGH":1},
	{"RACE":"Half-Elf","LOW":2,"HIGH":3},
	{"RACE":"Halfling","LOW":4,"HIGH":6},
	{"RACE":"Elf","LOW":7,"HIGH":9},
	{"RACE":"Human","LOW":10,"HIGH":89},
	{"RACE":"Dwarf","LOW":90,"HIGH":94},
	{"RACE":"Gnome","LOW":95,"HIGH":97},
	{"RACE":"Half-Orc","LOW":98,"HIGH":99},
	{"RACE":"Tiefling","LOW":100,"HIGH":100}
	)

def race(rroll, rtable):
	prace = ""
	for r in rtable:
	    if rroll >= r["LOW"] and rroll <= r["HIGH"]:
	        prace += r["RACE"]	
	return prace

def subrace(prace):
    srace = ""
    srace += dragonborn_sub(prace)
    srace += half_elf_sub(prace)
    srace += halfling_sub(prace)
    srace += elf_sub(prace)
    srace += human_sub(prace)
    srace += dwarf_sub(prace)
    srace += gnome_sub(prace)
    ##srace += half_orc_sub(prace)
    srace += tiefling_sub(prace) 
    return srace


def human_sub(prace):
    if prace != "Human":
        return ""
    else:
        sub = roll("1d10")
        if sub > 6:
            return "Specialist (Variant)"
        return "Generalist (Standard)"

def dwarf_sub(prace):
    if prace != "Dwarf":
        return ""
    else:
        sub = roll ("1d10")
        if sub <= 2:
           return "Gray"
        elif sub <= 5:
           return "Mountain"
        return "Hill"

def elf_sub(prace):
    if prace != "Elf":
        return ""
    else:
        sub = roll ("1d8")
        if sub == 1:
            return "Eladrin"
        elif sub <= 3:
            return "Drow"
        elif sub <= 5:
            return "Wood"
        return "High"

def halfling_sub(prace):
    if prace != "Halfling":
        return ""
    else:
        sub = roll("1d10")
        if sub == 1:
            return "Ghostwise"
        elif sub <= 5:
            return "Stout"
        return "Lightfoot"

def gnome_sub(prace):
    if prace != "Gnome":
        return ""
    else:
        sub = roll("1d10")
        if sub <= 2:
            return "Deep"
        elif sub <= 5:
            return "Forest"
        return "Rock"

def half_elf_sub(prace):
    if prace != "Half-Elf":
        return ""
    else:
        sub = roll("1d20")
        if sub <= 2:
            return "Half Eladrin"
        elif sub <= 4:
            return "Half Drow"
        elif sub <= 8:
            return "Half Wood Elf"
        elif sub <= 13:
            return "Half High Elf"
        return "Unkown Elven heritage"

def dragonborn_sub(prace):
    if prace != "Dragonborn":
        return ""
    else:
        sub = roll("1d10")
        if sub == 1:
            return "Black"
        elif sub == 2:
            return "Blue"
        elif sub == 3:
            return "Brass"
        elif sub == 4:
            return "Bronze"
        elif sub == 5:
            return "Copper"
        elif sub == 6:
            return "Gold"
        elif sub == 7:
            return "Green"
        elif sub == 8:
            return "Red"
        elif sub == 9:
            return "Silver"
        return "White"

def tiefling_sub(prace):
    if prace != "Tiefling":
        return ""
    else:
        sub = roll("1d12")
        if sub == 1:
            return "Blood of Asmodeus (Standard)"
        elif sub == 2:
            return "Blood of Baalzebul"
        elif sub == 3:
            return "Blood of Dispater"
        elif sub == 4:
            return "Feral"
        elif sub == 5:
            return "Feral (Variant)"
        elif sub == 6:
            return "Blood of Fierna"
        elif sub == 7:
            return "Blood of Glasya"
        elif sub == 8:
            return "Blood of Levistus"
        elif sub == 9:
            return "Blood of Mammon"
        elif sub == 10:
            return "Blood of Mephistopheles"
        elif sub == 11:
            return "Unknown (Variant)"
        return "Blood of Zariel"

primary_race = ""
sub_race = ""

primary_race = race(primary_roll, phb_race_table)
sub_race = subrace(primary_race)

race = primary_race + ": " + sub_race

formattedRace = " {} - " + race

print()
print(formattedRace.format(primary_roll))
print()

