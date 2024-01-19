"""
CS 5001
Final Project Bonus Part
Fall 2022
Chih-Tao Lee

Modify the original version of Puzzle().solvable_case() into the version which
is easier to test by Python Unittest
"""
"""
Because the original version involved with other functions (whenever the solvable
case was found, it would generate the puzzle in the Turtle automatically), it
would be easier to modify Puzzle().solvable_case() for further testings.

eg.
                               5  4  2
[5, 4, 2, 1, 3, 6, 7, 8, 9] =  1  3  6
                               7  8  9
9 is the blank piece
"""
import random
def solvable_case_tester(lst): # check if the given lst is solvable
    inversion_count = 0
    piece_num = len(lst) # the number of total pieces
    side_num = int(piece_num ** 0.5)

    for i in range(piece_num):
        if lst[i] == piece_num: # skip the blank piece
            continue
        for j in range(i, piece_num):
            if lst[j] == piece_num: # skip the blank piece
                continue
            if lst[i] > lst[j]:
                inversion_count += 1

    if piece_num % 2 != 0: # cases for odd piece_num
        if inversion_count % 2 == 0:
            return True # solvable
        else:
            return False # unsolvable
    else: # cases for even piece_num
        blank_indexx = lst.index(piece_num)
        row_num = blank_indexx // side_num
        if inversion_count % 2 == 0 and row_num % 2 == 1:
            return True # solvable
        elif inversion_count % 2 != 0 and row_num % 2 == 0:
            return True # solvable
        else:
            return False # unsolvable

def shuffle(lst): # this is a function to scramble the puzzle pieces
    for i in range(len(lst)):
        j = random.randint(0, len(lst) - 1)
        lst[i], lst[j] = lst[j], lst[i]

def solvable_case(piece_num, shuffle_func, test_func): # generate a solvable case

    lst = list(range(1, piece_num + 1)) # create the original list

    while True:
        shuffle_func(lst)
        if test_func(lst):
            break # break the loop when it's a solvable case
    return lst

"""
def solvable_case(self):
    self.create_thumbnail()
    h_length = int(self.info[2][1]) // 2
    piece_num = int(self.info[1][1])

    location = self.location(h_length)

    num_file = dict() # a dictionary to translate the assigned number of picture to its file name
    for i in self.info[4:]:
        num_file[int(i[0])] = i[1].strip(" ")

    def shuffle(lst): # this is a function to scramble the puzzle pieces
        for i in range(len(lst)):
            j = random.randint(0, len(lst) - 1)
            lst[i], lst[j] = lst[j], lst[i]

    def solvable_case_tester(lst): # this is a function to check if it's a solvable_case
        inversion_count = 0
        piece_num = len(lst) # the number of total pieces
        side_num = int(piece_num ** 0.5) # eg. 4 if piece_num = 16
        for i in range(piece_num):
            if lst[i] == piece_num: # skip the blank piece
                continue
            for j in range(i, piece_num): # skip the blank piece
                if lst[j] == piece_num:
                    continue
                if lst[i] > lst[j]:
                    inversion_count += 1
        if piece_num % 2 != 0: # cases for odd piece_num
            if inversion_count % 2 == 0:
                return True
            else:
                return False
        else: # cases for even piece_num
            blank_indexx = lst.index(piece_num)
            # check if the blank piece in the odd row or even row
            row_num = blank_indexx // side_num
            if inversion_count % 2 == 0 and row_num % 2 == 1:
                return True
            elif inversion_count % 2 != 0 and row_num % 2 == 0:
                return True
            else:
                return False

    lst = list(range(1, piece_num + 1)) # create the original list

    while True:
        shuffle(lst)
        if solvable_case_tester(lst):
            break # break the loop when it's a solvable case
"""
