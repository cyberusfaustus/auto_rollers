#!/usr/bin/env python

import unittest
import xdice
import race_roller

class PhBRaces(unittest.TestCase):

    def test_human_sub_race(self):
        race = "Human"
        subrace = race_roller.subrace(race)
        self.assertTrue(subrace == "Skilled (Standard)" or subrace == "Specialist (Variant)")

if __name__ == '__main__':
    unittest.main()	    
