#!/usr/bin/env python

import sys, getopt
from xdice import *
import backgroundNPC as bgNPC

class family:
   def __init__(self, parents, siblings):
      self.parents = parents
      self.siblings = siblings

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

def family_member_occupation():
    oroll = roll("1d100")
    if oroll < 6:
       return "Academic"
    elif oroll < 11:
       return "Adventurer: " + family_adventurer_class()
    elif oroll == 11:
       return "Aristocrat"
    elif oroll < 27:
       return "Artisan or guild member"
    elif oroll < 32:
       return "Criminal"
    elif oroll < 37:
       return "Entertainer"
    elif oroll < 39:
       return "Exile, hermit, or refugee"
    elif oroll < 44:
       return "Explorer or wanderer"
    elif oroll < 56:
       return "Farmer or herder"
    elif oroll < 61:
       return "Hunter or trapper"
    elif oroll < 76:
       return "Laborer"
    elif oroll < 81:
       return "Merchant"
    elif oroll < 86:
       return "Politician or bureaucrat"
    elif oroll < 91:
       return "Priest"
    elif oroll < 96:
       return "Sailor"
    else:
       return "Soldier"

def family_adventurer_class():
    croll = roll("1d100")
    if croll < 8:
       return "Barbarian"
    elif croll < 15:
       return "Bard"
    elif croll < 30:
       return "Cleric"
    elif croll < 37:
       return "Druid"
    elif croll < 53:
       return "Fighter"
    elif croll < 59:
       return "Monk"
    elif croll < 65:
       return "Paladin"
    elif croll < 71:
       return "Ranger"
    elif croll < 85:
       return "Rogue"
    elif croll < 90:
       return "Sorcerer"
    elif croll < 95:
       return "Warlock"
    else:
       return "Wizard"

def family_member_alignment():
    aroll = roll("3d6")
    split = roll("1d2")
    if aroll < 4:
       if split == 1:
          return "Chaotic evil"
       else:
          return "Chaotic neutral"
    elif aroll < 6:
       return "Lawful evil"
    elif aroll < 9:
       return "Neutral evil"
    elif aroll < 13:
       return "Neutral"
    elif aroll < 16:
       return "Neutral good"
    elif aroll < 18:
       if split == 1:
          return "Lawful good"
       else:
          return "Lawful neutral"
    else:
       if split == 1:
          return "Chaotic good"
       else:
          return "Chaotic neutral"

def family_member_relationship():
    rel = roll("3d4")
    if rel < 5:
       return "Hostile"
    elif rel < 11:
       return "Friendly"
    else:
       return "Indifferent"

def family_member_status():
    status = roll("3d6")
    if status < 4:
       return "Dead: " + member_cause_of_death()
    elif status < 6:
       return "Missing or unknown"
    elif status < 9:
       return "Alive, but doing poorly due to injury, financial trouble or relationship difficulties"
    elif status < 13:
       return "Alive and well"
    elif status < 16:
       return "Alive and quite successful"
    elif status < 18:
       return "Alive and infamous"
    else:
       return "Alive and famous"

def member_cause_of_death():
    cause = roll("1d12")
    if cause == 1:
       return "Unkown"
    elif cause == 2:
       return "Murdered"
    elif cause == 3:
       return "Killed in battle"
    elif cause == 4:
       return "Accident related to class or occupation"
    elif cause == 5:
       return "Accident unrelated to class or occupation"
    elif cause < 8:
       return "Natural causes, such as disease or old age"
    elif cause == 8:
       return "Apparent suicide"
    elif cause == 9:
       return "Torn apart by an animal or a natural disaster"
    elif cause == 10:
       return "Consumed by a monster"
    elif cause == 11:
       return "Executed for a crime or tortured to death"
    else:
       return "Bizarre event, such as being hit by a meteorite, struck down by an angry god or killed by a hatching slaad egg"

def number_of_siblings():
    sibs = roll("1d10")
    if sibs < 3:
       return 0
    elif sibs < 5:
       return roll("1d3")
    elif sibs < 7:
       return roll("1d4+1")
    elif sibs < 9:
       return roll("1d6+2")
    else:
       return roll("1d8+3")

def birth_order():
    order = roll("2d6")
    if order == 2:
       return "Twin, triplet, or quadruplet"
    elif order < 8:
       return "Older"
    else:
       return "Younger"

def member_details(member):
    member.occupation = family_member_occupation()
    member.alignment = family_member_alignment()
    member.relationship = family_member_relationship()
    member.status = family_member_status()

def detail_members(members):
    for member in members:
       member_details(member)

def print_members(member_group):
    for member in member_group:
        print(member.relation)
        print(member.occupation)
        print(member.alignment)
        print(member.relationship)
        print(member.status)
        print()

def main(argv):
    
    print("-----------------------------")
    print_parents_known(parents_known())
    parents = [bgNPC.BackgroundNPC("Father"), bgNPC.BackgroundNPC("Mother")]
    detail_members(parents)
    print_members(parents)   
 
    num_of_sibs = number_of_siblings()
    print("You have {} siblings".format(num_of_sibs))
    siblings = []
    for x in range(num_of_sibs):
        siblings.append(bgNPC.BackgroundNPC(birth_order() + " Sibling"))
    detail_members(siblings)
    print_members(siblings)

if __name__ =="__main__":
    main(sys.argv[1:])

