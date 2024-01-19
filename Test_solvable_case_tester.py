"""
CS 5001
Final Project Bonus Part
Fall 2022
Chih-Tao Lee

Testing solvable_case_tester function
"""
import unittest
from solvable_case import *
class TestSolvableCaseTester(unittest.TestCase):
    
    def setUp(self):
        # case 1: 4*4 solvable
        self.lst_16_1 = [11, 15, 3, 10, 12, 1, 6, 14, 8, 4, 9, 5, 7, 13, 2, 16]
        # case 2: 4*4 unsolvable
        self.lst_16_2 = [15, 3, 2, 8, 13, 11, 9, 5, 12, 6, 14, 1, 16, 7, 4, 10]
        # case 3: 3*3 solvable
        self.lst_9_1 = [8, 1, 2, 7, 9, 4, 5, 6, 3]
        # case 4: 3*3 unsolvable
        self.lst_9_2 = [7, 4, 8, 6, 3, 1, 9, 5, 2]
        # case 5: 2*2 solvable
        self.lst_4_1 = [2, 3, 4, 1]
        # case 6: 2*2 unsolvable
        self.lst_4_2 = [1, 3, 2, 4]

    def test_solvable_case_tester(self):
        self.assertEqual(solvable_case_tester(self.lst_16_1), True) # case 1
        self.assertEqual(solvable_case_tester(self.lst_16_2), False) # case 2
        self.assertEqual(solvable_case_tester(self.lst_9_1), True) # case 3
        self.assertEqual(solvable_case_tester(self.lst_9_2), False) # case 4
        self.assertEqual(solvable_case_tester(self.lst_4_1), True) # case 5
        self.assertEqual(solvable_case_tester(self.lst_4_2), False) # case 6

if __name__ == "__main__":
    unittest.main()
