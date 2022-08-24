#!/usr/bin/env python

import sys, getopt
from xdice import * 

a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0

def roll_attr():
    rolls = []
    for x in range(4):
        rV = roll("1d6")
        if rV == 1:
            rv = roll("1d6")
        rolls.append(rV)

    rolls.sort()
    rolls.pop(0)

    attr = 0
    for r in rolls:
        attr += r
    return attr
           

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

def attribute_total(char_attrs):
    score = 0
    for a in char_attrs.values():
       score += a
    return score

def isBiggerAttrs(a, b):
    aTotal = attribute_total(a)
    bTotal = attribute_total(b)
    return aTotal > bTotal

def generate():
    char_attrs = {}
    char_attrsTemp = {}

    print("|Roll #|STR|DEX|CON|INT|WIS|CHA|")
    print("|:----:|:-:|:-:|:-:|:-:|:-:|:-:|")

    for x in range(3):
        char_attrsTemp = roll_char_attrs()
        #printAttr(char_attrsTemp)
        #print(char_attrsTemp)
        #print()
        formattedAttribs= "|Roll {}|{}|{}|{}|{}|{}|{}|"
        print(formattedAttribs.format(x+1, char_attrsTemp["STR"], char_attrsTemp["DEX"], char_attrsTemp["CON"], char_attrsTemp["INT"], char_attrsTemp["WIS"], char_attrsTemp["CHA"]))        
       
        if isBiggerAttrs(char_attrsTemp, char_attrs):
            char_attrs = char_attrsTemp

    return char_attrs

def printAttr(char_attrs):
    for k, v in char_attrs.items():
        formatedAttrib = " {}:  {}"
        print(formatedAttrib.format(k,v))

    
