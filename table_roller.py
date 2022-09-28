
import sys, getopt, os, csv
from xdice import * 


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


