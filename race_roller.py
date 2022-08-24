#!/usr/bin/env python

import sys, getopt, os, csv
import table_roller
from xdice import * 

def load_race_table(fname):
    with open(fname, "r") as f:
        csv_reader = csv.DictReader(f)
        race_table = list(csv_reader)
        ensureIntDemographicData(race_table)
        return race_table

def ensureIntDemographicData(race_table):
    for r in race_table:
        r["LOW"] = int(r["LOW"])
        r["HIGH"] = int(r["HIGH"])


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

