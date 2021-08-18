#!/usr/bin/env python

import unittest
import xdice
import race_roller

class PhBRaces(unittest.TestCase):
    def test_phb_human_low_roll(self):
        race = race_roller.race(10, race_roller.phb_race_table)
        self.assertEqual(race, "Human")

    def test_phb_human_high_roll(self):
        race = race_roller.race(89, race_roller.phb_race_table)
        self.assertEqual(race, "Human")

    def test_phb_human_mid_roll(self):
        race = race_roller.race(50, race_roller.phb_race_table)
        self.assertEqual(race, "Human")

    def test_not_a_phb_human(self):
        race = race_roller.race(9, race_roller.phb_race_table)
        self.assertNotEqual(race, "Human")
        race = race_roller.race(90, race_roller.phb_race_table)
        self.assertNotEqual(race, "Human")


    def test_human_sub_race(self):
        race = "Human"
        subrace = race_roller.subrace(race)
        self.assertTrue(subrace == "Generalist (Standard)" or subrace == "Specialist (Variant)")

if __name__ == '__main__':
    unittest.main()	    
