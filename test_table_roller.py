#!/usr/bin/env python

import unittest
import xdice
import table_roller

class TestTableRoller(unittest.TestCase):
    def test_load_table_data(self):
        actual = table_roller.load_table_data("./roll_tables/test_tables/test_table1.csv")
        expectedRow = {"NAME": "Bilbo","LOW": "1","HIGH": "10"}
        self.assertEqual(actual[0], expectedRow)

    def test_load_table(self):
        actual = table_roller.load_table("./roll_tables/test_tables/test_table1.csv")
        expectedRow = {"NAME": "Bilbo","LOW":1,"HIGH":10}
        self.assertEqual(actual[0], expectedRow)

    def test_pick_from_table(self):
        table = table_roller.load_table("./roll_tables/test_tables/test_table1.csv")
        actual = table_roller.pick_from_table(12,table)
        expected = "Frodo"
        self.assertEqual(actual, expected)

    def test_get_die_from_last_entry(self):
        tableData = table_roller.load_table_data("./roll_tables/test_tables/test_table1.csv")
        actual = table_roller.get_die_from_last_entry(tableData)
        expected = "20"
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()    
