#!/usr/bin/env python

import sys, getopt, os, csv
import table_roller
from xdice import * 

def checkForCSV(fname):
    root, ext = os.path.splitext(fname)
    if ext == ".csv":
        return True
    return False

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
    srace += drow_sub(prace)
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
        return table_roller.roll_on_table("./roll_tables/subraces/humans.csv")

def dwarf_sub(prace):
    if prace != "Dwarf":
        return ""
    else:
        return table_roller.roll_on_table("./roll_tables/subraces/dwarves.csv")
        sub = roll ("1d10")

def elf_sub(prace):
    if prace != "Elf":
        return ""
    else:
        return table_roller.roll_on_table("./roll_tables/subraces/elves.csv")

def drow_sub(prace):
    if prace != "Drow":
        return ""
    else:
       return table_roller.roll_on_table("./roll_tables/subraces/drows.csv")


def halfling_sub(prace):
    if prace != "Halfling":
        return ""
    else:
        return table_roller.roll_on_table("./roll_tables/subraces/halflings.csv")

def gnome_sub(prace):
    if prace != "Gnome":
        return ""
    else:
        return table_roller.roll_on_table("./roll_tables/subraces/gnomes.csv")

def half_elf_sub(prace):
    if prace != "Half-Elf":
        return ""
    else:
        return table_roller.roll_on_table("./roll_tables/subraces/halfelves.csv")

def dragonborn_sub(prace):
    if prace != "Dragonborn":
        return ""
    else:
        return table_roller.roll_on_table("./roll_tables/subraces/dragonborn.csv")

def tiefling_sub(prace):
    if prace != "Tiefling":
        return ""
    else:
        return table_roller.roll_on_table("./roll_tables/subraces/tieflings.csv")

def ancestry(primary_race):
    sub_race = subrace(primary_race)
    return primary_race + ": " + sub_race

def print_ancestry_from_file(fname):
    table = table_roller.load_table_data(fname)
    die = table_roller.get_die_from_last_entry(table)
    table_roller.ensureIntLowHighData(table)
    primary_roll = roll("1d"+die)
    primary_race = table_roller.pick_from_table(primary_roll, table)
    formattedRace = " {} - " + ancestry(primary_race)
    print()
    print(formattedRace.format(primary_roll))
    print() 

def main(argv):
    table_choice = ''
    helpText = "race_roller.py -d <demographic_table>\n"\
               "-d   optional, accepted values include:\n"\
               "     P : uses Player's Handbook Races (Default)\n"\
               "     B : uses Basic Four Races\n"\
               "     <filename>.csv : CSV file containing custom demographics\n\n"\
               "-------------------------------------------------------------\n"\
               "CSV file first line must have headers RACE,LOW,HIGH\n"\
               "designating the race and the low and high d100 values for\n"\
               "the demographic.\n"\
               "Races with Supported sub-race calculation:\n"\
               "Dragonborn\n"\
               "Half-Elf\n"\
               "Halfling\n"\
               "Elf\n"\
               "Human\n"\
               "Dwarf\n"\
               "Gnome\n"\
               "Tiefling\n"\

    try:
        opts, args = getopt.getopt(argv, "hd:")
    except getopt.GetoptError:
        print(helpText)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(helpText)
            sys.exit()
        elif opt == '-d':
            table_choice = str(arg)

    if table_choice == "B":
        print_ancestry_from_file("./roll_tables/demographics/basic_four.csv")
    elif checkForCSV(table_choice):
        print_ancestry_from_file(table_choice)
    else:
        print_ancestry_from_file("./roll_tables/demographics/phb_races_swordcoast.csv")

if __name__ == "__main__":
    main(sys.argv[1:])

