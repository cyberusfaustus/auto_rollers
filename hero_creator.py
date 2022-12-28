#!/usr/bin/env python

from xdice import *
import time
import race_roller as rroller
import colville_char_roller as croller
import table_roller


cls = chr(27)+"[H" + chr(27) + "[J"
print(cls)
print()
time.sleep(1)
print(".", end='')
print()
print("A booming voice anounces:")
print("    \"It has been decreed: a new hero shall enter the planes\"")
time.sleep(1)
print(".", end='')
time.sleep(1)
print(".", end='')
print()
print("... Thunder rolls portentiously ...")
table = table_roller.load_table_data("./roll_tables/demographics/phb_races_swordcoast.csv")
die = table_roller.get_die_from_last_entry(table)
table_roller.ensureIntLowHighData(table)
primary_roll = roll("1d"+die)
primary_race = table_roller.pick_from_table(primary_roll, table)
ancestry = rroller.ancestry(primary_race)
time.sleep(1)
print(".", end='')
time.sleep(1)
print(".", end='')
print()
print("    \"A new " + ancestry + " has been born\"")
attribs = croller.generate()
print("    \"And they shall have the following attributes:\"")
#print(attribs)
print()
for k, v in attribs.items():
    formatedAttrib = "       {}:  {} - " + v.format(verbose=True)
    print(formatedAttrib.format(k,v))
print()
time.sleep(1)
print(".", end='')
time.sleep(1)
print(".", end='')
print()
print("    \"They shall certainly be great, yet their course is undetermined... \"")
print("          \"They would be good in any of these professions:\"")

sClasses = croller.suggestedClasses(attribs)
print("                  " + sClasses)

