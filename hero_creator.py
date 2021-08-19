#!/usr/bin/env python

import xdice
import time
import race_roller as rroller
import colville_char_roller as croller

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
rroll = xdice.roll("1d100")
ancestry = rroller.ancestry(rroll, rroller.phb_race_table)
time.sleep(1)
print(".", end='')
time.sleep(1)
print(".", end='')
print()
print("    \"A new " + ancestry + " has been born\"")
attribs = croller.generate()
print("    \"And they shall have the following attributes:\"")
print(attribs)
time.sleep(1)
print(".", end='')
time.sleep(1)
print(".", end='')
print()
print("    \"They shall certainly be great, yet their course is undetermined... \"")
print("          \"They would be good in any of these professions:\"")

sClasses = croller.suggestedClasses(attribs)
print(sClasses)

