#!/usr/bin/env python

from xdice import * 

a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0

def roll_attr():
    return roll("4d6L1")

def roll_char_attrs():
    STR = roll_attr()
    DEX = roll_attr()
    CON = roll_attr()
    INT = roll_attr()
    WIS = roll_attr()
    CHA = roll_attr()

    return {
            "STR":STR,
            "DEX":DEX,
            "CON":CON,
            "INT":INT,
            "WIS":WIS,
            "CHA":CHA
            }

def isWorthy(char_attrs):
    counter = 0
    for a in char_attrs.values():
        if isHeroicAttribute(a):
            counter += 1
    return counter > 1

def generate():
    heroFound = False
    char_attrs = {}
    while heroFound == False:
        char_attrs = roll_char_attrs()
        heroFound = isWorthy(char_attrs)

    return char_attrs

def createFromList(attrs):
    STR = attrs[0]
    DEX = attrs[1]
    CON = attrs[2]
    INT = attrs[3]
    WIS = attrs[4]
    CHA = attrs[5]

    return {
            "STR":STR,
            "DEX":DEX,
            "CON":CON,
            "INT":INT,
            "WIS":WIS,
            "CHA":CHA
            }

def isHeroicAttribute(attribute):
    if attribute > 14:
        return True
    return False

def oneIsHeroicAttribute(a1, a2):
    return isHeroicAttribute(a1) or isHeroicAttribute(a2)

def areHeroicAttributes(a1, a2):
    return isHeroicAttribute(a1) and isHeroicAttribute(a2)

def isGoodFighter(char_attrs):
    return oneIsHeroicAttribute(char_attrs["STR"], char_attrs["DEX"])

def isGoodWizard(char_attrs):
    return isHeroicAttribute(char_attrs["INT"])

def isGoodRogue(char_attrs):
    return isHeroicAttribute(char_attrs["DEX"])

def isGoodCleric(char_attrs):
    return isHeroicAttribute(char_attrs["WIS"])

def isGoodRanger(char_attrs):
    return areHeroicAttributes(char_attrs["DEX"], char_attrs["WIS"])

def isGoodPaladin(char_attrs):
    return areHeroicAttributes(char_attrs["STR"], char_attrs["CHA"])

def isGoodMonk(char_attrs):
    return areHeroicAttributes(char_attrs["DEX"], char_attrs["WIS"])

def isGoodBarbarian(char_attrs):
    return isHeroicAttribute(char_attrs["STR"])

def isGoodBard(char_attrs):
    return isHeroicAttribute(char_attrs["CHA"])

def isGoodDruid(char_attrs):
    return isHeroicAttribute(char_attrs["WIS"])

def isGoodSorcerer(char_attrs):
    return isHeroicAttribute(char_attrs["CHA"])

def isGoodWarlock(char_attrs):
    return isHeroicAttribute(char_attrs["CHA"])


def suggestedClasses(c):
    classes = ""
    if isGoodFighter(c):
        classes += "Fighter "

    if isGoodWizard(c):
        classes += "Wizard "
 
    if isGoodRogue(c):
        classes += "Rogue "

    if isGoodCleric(c):
        classes += "Cleric "

    if isGoodRanger(c):
        classes += "Ranger "

    if isGoodPaladin(c):
        classes += "Paladin "

    if isGoodMonk(c):
        classes += "Monk "

    if isGoodBarbarian(c):
        classes += "Barbarian "

    if isGoodBard(c):
        classes += "Bard "

    if isGoodDruid(c):
        classes += "Druid "

    if isGoodSorcerer(c):
        classes += "Sorcerer "

    if isGoodWarlock(c):
        classes += "Warlock "

    return classes

colvilleChar = generate()

print("-----------------------------")
# print("-STR-DEX-CON-INT-WIS-CHA-")  
# print(colvilleChar.values())
print()
for k, v in colvilleChar.items():
    formatedAttrib = " {}:  {} - " + v.format(verbose=True)

    print(formatedAttrib.format(k,v))
print()
print("Suggested Classes:")
print(suggestedClasses(colvilleChar))

print()



    
