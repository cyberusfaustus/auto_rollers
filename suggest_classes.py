#!/usr/bin/env python


import colville_char_roller as croller

attribs =[]
print()
print()
print("Enter your attributes in order below.")
print()
attribs.append(int(input("STR: ")))
attribs.append(int(input("DEX: ")))
attribs.append(int(input("CON: ")))
attribs.append(int(input("INT: ")))
attribs.append(int(input("WIS: ")))
attribs.append(int(input("CHA: ")))

character = croller.createFromList(attribs)
print()
#print()
#for k, v in character.items():
#    formattedAttrib = " {}:  {}"
#    print(formattedAttrib.format(k,v))

print()
print("Suggested Classes: ")
print(croller.suggestedClasses(character))
print()


