#!/usr/bin/env python

import triple_attribute_set_roller as troller
import colville_char_roller as croller

print("### Hero")
character = troller.generate()
print()
print("--------------------------------")
print("## Attributes Used")
print("--------------------------------")

for k, v in character.items():
    formattedAttrib = " {}:  {}"
    print(formattedAttrib.format(k,v))

print()
print("--------------------------------")
print("## Suggested Classes: ")
print(croller.suggestedClasses(character))
print("--------------------------------")
print()


