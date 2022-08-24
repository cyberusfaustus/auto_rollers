#!/usr/bin/env python

import sys, getopt
from xdice import *
import backgroundNPC as bgNPC

def parents_known():
    p_roll = roll("1d100")
    if p_roll < 96:
       return True
    return False

def print_parents_known(parents_known):
    if parents_known:
       print("You know who your parents are or were.")
    else:
       print("You do not know who your parents were.")

def main(argv):

    print("-----------------------------")
    print_parents_known(parents_known())

if __name__ =="__main__":
    main(sys.argv[1:])

