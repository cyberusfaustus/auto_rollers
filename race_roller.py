#!/usr/bin/env python

from xdice import * 

primary_roll  = roll("1d100")

primary_table = {
        "HUMAN":50,
        "DWARF":60,
        "ELF":70,
        "HALFLING":80,
        "GNOME":84,
        "HALF-ELF":88,
        "GOLIATH":90,
        "DRAGONBORN":92,
        "HALF-ORC":94,
        "TIEFLING":96,
        "AASIMAR":98,
        "AARAKOCRA":99,
        "GENASI":100
        }

def human_sub():
    sub = roll("1d10")
    if sub > 6:
        return "Specialist (Variant)"
    return "Generalist (Standard)"

def dwarf_sub():
    sub = roll ("1d10")
    if sub <= 2:
        return "Gray"
    elif sub <= 5:
        return "Mountain"
    return "Hill"

def elf_sub():
    sub = roll ("1d8")
    if sub == 1:
        return "Eladrin"
    elif sub <= 3:
        return "Drow"
    elif sub <= 5:
        return "Wood"
    return "High"

def halfling_sub():
    sub = roll("1d10")
    if sub == 1:
        return "Ghostwise"
    elif sub <= 5:
        return "Stout"
    return "Lightfoot"

def gnome_sub():
    sub = roll("1d10")
    if sub <= 2:
        return "Deep"
    elif sub <= 5:
        return "Forest"
    return "Rock"

def half_elf_sub():
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

def dragonborn_color():
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


primary_race = ""

if primary_roll <= primary_table["HUMAN"]:
    primary_race = "Human: " + human_sub()
elif primary_roll <= primary_table["DWARF"]:
    primary_race = "Dwarf: " + dwarf_sub()
elif primary_roll <= primary_table["ELF"]:
    primary_race = "Elf: " + elf_sub()
elif primary_roll <= primary_table["HALFLING"]:
    primary_race = "Halfling: " + halfling_sub()
elif primary_roll <= primary_table["GNOME"]:
    primary_race = "Gnome: " + gnome_sub() 
elif primary_roll <= primary_table["HALF-ELF"]:
    primary_race = "Half-Elf: " + half_elf_sub()
elif primary_roll <= primary_table["GOLIATH"]:
    primary_race = "Goliath"
elif primary_roll <= primary_table["DRAGONBORN"]:
    primary_race = "Dragonborn: Color -  " + dragonborn_color()
elif primary_roll <= primary_table["HALF-ORC"]:
    primary_race = "Half-Orc"
elif primary_roll <= primary_table["TIEFLING"]:
    primary_race = "Tiefling"
elif primary_roll <= primary_table["AASIMAR"]:
    primary_race = "Aasimar"
elif primary_roll <= primary_table["AARAKOCRA"]:
    primary_race = "Aarakocra"
elif primary_roll <= primary_table["GENASI"]:
    primary_race = "Genasi"

formattedRace = " {} - " + primary_race

print()
print(formattedRace.format(primary_roll))
print()


