"""
CS 5001
Final Project Bonus Part
Fall 2022
Chih-Tao Lee

Testing solvable_case function
"""
import unittest
from solvable_case import *
class TestSolvableCase(unittest.TestCase):

    def setUp(self):
        # generate two solvable sequences for 4*4 format
        self.lst_16_1 = solvable_case(16, shuffle, solvable_case_tester)
        self.lst_16_2 = solvable_case(16, shuffle, solvable_case_tester)
        print(self.lst_16_1) # print the two sequences in the terminal
        print(self.lst_16_2)
        # generate two solvable sequences for 3*3 format
        self.lst_9_1 = solvable_case(9, shuffle, solvable_case_tester)
        self.lst_9_2 = solvable_case(9, shuffle, solvable_case_tester)
        print(self.lst_9_1) # print the two sequences in the terminal
        print(self.lst_9_2)
        # generate two solvable sequences for 2*2 format
        self.lst_4_1 = solvable_case(4, shuffle, solvable_case_tester)
        self.lst_4_2 = solvable_case(4, shuffle, solvable_case_tester)
        print(self.lst_4_1) # print the two sequences in the terminal
        print(self.lst_4_2)

    def test_solvable_case(self):
        self.assertEqual(solvable_case_tester(self.lst_16_1), True)
        self.assertEqual(solvable_case_tester(self.lst_16_2), True)
        self.assertEqual(solvable_case_tester(self.lst_9_1), True)
        self.assertEqual(solvable_case_tester(self.lst_9_2), True)
        self.assertEqual(solvable_case_tester(self.lst_4_1), True)
        self.assertEqual(solvable_case_tester(self.lst_4_2), True)

if __name__ == "__main__":
    unittest.main()
