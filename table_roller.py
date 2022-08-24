
import sys, getopt, os, csv
from xdice import * 

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

basic_four_table = (
        {"RACE":"Halfling","LOW":1,"HIGH":10},
        {"RACE":"Elf","LOW":11,"HIGH":25},
        {"RACE":"Human","LOW":26,"HIGH":75},
        {"RACE":"Dwarf","LOW":76,"HIGH":100}
        )

def load_table(fname):
    table = load_table_data(fname)
    ensureIntLowHighData(table)
    return table

def load_table_data(fname):
    with open(fname, "r") as f:
        csv_reader = csv.DictReader(f)
        table = list(csv_reader)
        return table

def ensureIntLowHighData(table):
    for r in table:
        r["LOW"] = int(r["LOW"])
        r["HIGH"] = int(r["HIGH"])


def checkForCSV(fname):
    root, ext = os.path.splitext(fname)
    if ext == ".csv":
        return True
    return False

def pick_from_table(num, table):
    value = ""
    keys = table[0].keys()
    key = ""
    for k in keys:
        key = k
        break
    for r in table:
        if num >= r["LOW"] and num <= r["HIGH"]:
            value += r[key]
    return value
    
def get_die_from_last_entry(tableData):
    die = ""
    i = 0
    for r in tableData:
        if i==len(tableData)-1:
            die = r["HIGH"]
        i+=1
    return die

def roll_on_table(fname):
    table = load_table_data(fname)
    die = get_die_from_last_entry(table)
    ensureIntLowHighData(table)
    troll = roll("1d"+die)
    return pick_from_table(troll, table)


