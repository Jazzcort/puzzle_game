"""
CS 5001
Final Project
Fall 2022
Chih-Tao Lee

Design a sliding puzzle game
"""
from turtle import *
from datetime import datetime
import random
import os
import time
class Frame(object):
    """
    This is a class to create three main frames in the game
    self.paint() will make the class start drawing the frame
    """
    def __init__(self, height=0, width=0, position=[0,0]):
        self.height = height
        self.width = width
        self.position = position
    def paint(self, color="black"):
        a = Turtle(visible=False)
        a.speed(10)
        a.penup()
        a.setposition(self.position[0], self.position[1])
        a.pendown()
        a.width(8)
        a.color(color)
        a.forward(self.width)
        a.right(90)
        a.forward(self.height)
        a.right(90)
        a.forward(self.width)
        a.right(90)
        a.forward(self.height)

class Puzzle(object):
    """
    This class is like a set of puzzle pieces
    self.info is a list format data from the given .puz file
    self.register_pic() is a function to register the picture of each puzzle piece
    self.puz is a list data structure to store all the Pieces classes as puzzle pieces
    self.blank is the index of the blank piece in self.puz
    self.e_pieces stores the index of the adjacent pieces to the blank piece as a list format
    self.solvable_case() is a function to create a solvable and scrambled sequence of puzzle pieces
    self.effective_area() is a function to update self.e_pieces after every switch
    self.location() is a function to calculate the position of each puzzle pieces depending on the
    picture size
    self.create_thumbnail() is a function to create a thumbnail picture on the top right conner
    self.reset() is a function to create a unscrambled sequence of the puzzle pieces
    self.move_order() is a function to swap the positions of two Pieces classes in self.puz
    self.clear_all() is a function to clear all the puzzle pieces in the window
    """
    def __init__(self, info):
        self.info = info
        self.register_pic()
        self.puz = []
        self.blank = 0
        self.e_pieces = []
        self.solvable_case()
        self.effective_area()

    def register_pic(self):
        for i in self.info[3:]:
            Screen().register_shape(i[1].strip(" "))

    def location(self, h_length):
        lst = []
        times = int(int(self.info[1][1]) ** 0.5)
        for i in range(times):
            for j in range(times):
                lst.append([-400 + h_length + j * 2 * h_length + j * 2, 400 - h_length - 2 * i * h_length - 2 * i])
        return lst

    def effective_area(self):
        self.e_pieces = []
        # for 16 pieces puzzle
        dic_16 = {0: [1, 4],  # indices of the adjacent pieces to the blank piece located at index 0
                  1: [0, 2, 5],
                  2: [1, 3, 6],
                  3: [2, 7],
                  4: [0, 5, 8],
                  5: [1, 4, 6, 9],
                  6: [2, 5, 7, 10],
                  7: [3, 6, 11],
                  8: [4, 9, 12],
                  9: [5, 8, 10, 13],
                  10: [6, 9, 11, 14],
                  11: [7, 10, 15],
                  12: [8, 13],
                  13: [9, 12, 14],
                  14: [10, 13, 15],
                  15: [11, 14]}
        # for 9 pieces puzzle
        dic_9 = {0: [1, 3],
                 1: [0, 2, 4],
                 2: [1, 5],
                 3: [0, 4, 6],
                 4: [1, 3, 5, 7],
                 5: [2, 4, 8],
                 6: [3, 7],
                 7: [4, 6, 8],
                 8: [5, 7]}
        # for 4 pieces puzzle
        dic_4 = {0: [1, 2],
                 1: [0, 3],
                 2: [0, 3],
                 3: [1, 2]}
        if int(self.info[1][1]) == 16:
            self.e_pieces = dic_16[self.blank]
        if int(self.info[1][1]) == 9:
            self.e_pieces = dic_9[self.blank]
        if int(self.info[1][1]) == 4:
            self.e_pieces = dic_4[self.blank]

    def create_thumbnail(self):
        self.thumb_n = Turtle(visible=False)
        self.thumb_n.penup()
        self.thumb_n.setposition(380, 400)
        self.thumb_n.shape(self.info[3][1].strip(" "))
        self.thumb_n.st()

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
            print(lst)
            if solvable_case_tester(lst):
                print("solvable")
                print("------------------------------------")
                break # break the loop when it's a solvable case
            print("unsolvable")

        for order, i in enumerate(lst): # create the puzzle with the solvable sequence
            if i == piece_num:
                self.blank = order # get the index of the blank piece
            self.puz.append(Pieces(i, num_file[i], location[order], h_length))

    def reset(self):
        h_length = int(self.info[2][1]) // 2
        self.puz = []

        num_file = dict()
        for i in self.info[4:]:
            num_file[int(i[0])] = i[1].strip(" ")

        location = self.location(h_length)
        blank_num = int(self.info[1][1])

        for order, i in enumerate(range(1, blank_num + 1)):
            if i == blank_num:
                self.blank = order # assign the index of the blank piece to self.blank
            self.puz.append(Pieces(i, num_file[i], location[order], h_length))

        self.effective_area() # update self.e_pieces

    def move_order(self, num1, num2):
        self.puz[num1].move(self.puz[num2])
        self.puz[num1], self.puz[num2] = self.puz[num2], self.puz[num1]
        self.blank = num2
        self.effective_area() # update self.e_pieces

    def clear_all(self):
        for i in self.puz:
            i.tur.ht()

class Pieces(object):
    """
    This class is like a Turtle object with more information
    It acts like a sigle piece of a puzzle
    self.num represents the picture number
    self.pic is the file directory of the picture
    self.position represents the its position ([x-axis, y-axis])
    self.tur is a Trutle object which can switch its position with other Pieces classes
    self.h_length is an integer represents the half of the picture's side length
    self.area stores the range of x-axis and y-axis of the piece's area
    self.create_turtle() is a function that creates self.tur for each Pieces class
    self.set_area() update self.area with self.position
    self.move() is a function that can switch two Pieces classes' position
    """
    def __init__(self, num=-1, pic="", position=[0,0], h_length=0):
        self.num = num
        self.pic = pic
        self.position = position
        self.h_length = h_length
        self.area = [0, 0]
        self.create_turtle()
        self.set_area()

    def create_turtle(self): # create a Turtle object with the given picture and position
        self.tur = Turtle(visible=False)
        self.tur.shape(self.pic)
        self.tur.penup()
        self.tur.speed(10)
        self.tur.setposition(self.position[0], self.position[1])
        self.tur.st()

    def move(self, other): # switch two puzzle pieces
        self.position, other.position = other.position, self.position
        self.tur.setposition(self.position[0], self.position[1])
        other.tur.setposition(other.position[0], other.position[1])
        self.set_area() # update self.area
        other.set_area() # update self.area

    def set_area(self): # calculate the range of self.area
        [x, y] = self.position
        self.area[0] = ([x - self.h_length, x + self.h_length])
        self.area[1] = ([y - self.h_length, y + self.h_length])

class LeaderBoard(object):
    """
    This is a class to load, print, and update the leaderboard.txt
    self.leaders contains the winners' name and steps they used and it's sorted
    by the steps they used to solve the puzzle
    self.load_leaderboard() is a function that load the leaders' from
    "leaderboard.txt"
    self.show_leadervoard() is a function that print the leaders in the window
    self.update_leaders() is a function that update "leaderboard.txt" when
    someone win the game
    """
    def __init__(self):
        self.leaders= []
        self.load_leaderboard()
        self.show_leaderboard()

    def load_leaderboard(self):
        try: # load leaders from "leaderboard.txt"
            with open("leaderboard.txt", mode="r") as r_file:
                for i in r_file:
                    self.leaders.append(i.strip("\n"))
                    if len(self.leaders) >= 15: # only load the first 15 leaders
                        break
        except FileNotFoundError: # "leaderboard.txt" not found
            error_msg = Turtle(visible=False)
            error_msg.shape("Resources/leaderboard_error.gif")
            error_msg.st()
            time.sleep(3)
            error_msg.ht()
            with open("5001_puzzle.err", mode="a") as a_file: # update error log
                dt = datetime.now()
                cur = dt.strftime("%a, %b %d, %Y, %H:%M:%S ")
                err_log = (cur + "Error: Could not open leaderboard.txt " +
                           "LOCATION: LeaderBoard.load_leaderboard()\n")
                a_file.write(err_log)

    def show_leaderboard(self): # print leaders in the game window
        location = [350 - x * 35 for x in range(len(self.leaders))]
        pen = Turtle(visible=False)
        pen.penup()
        pen.setposition(160, 380)
        pen.write("Leaders:", False, align="left",
                  font=("Arial", 22, "normal"))
        pen.pencolor("blue")
        for order, i in enumerate(location):
            pen.setposition(175, i)
            pen.write(self.leaders[order], False, align="left",
                      font=("Arial", 20, "normal"))

    def update_leaders(self, name, steps): # update "leaderboard.txt"
        leader_compare = [0] * 15
        for order, i in enumerate(self.leaders):
            leader_compare[order] = i.split(":")
        for order, i in enumerate(leader_compare):
            if i == 0: # when leaders are less than 15
                self.leaders.append(f"{name}: {steps}")
                break
            if int(i[1]) > steps:
                self.leaders.insert(order, f"{name}: {steps}")
                break
        if len(self.leaders) > 15:
            self.leaders.pop() # erase the 16th winner
        with open("leaderboard.txt", mode="w") as w_file: # overwrite "leaderboard.txt"
            for i in self.leaders:
                w_file.write(i + '\n')

class Game(object):
    """
    This is a class to connect all the other classes and acts like a game driver
    self.x represents the x-axis gathered from Screen().onclick()
    self.y represents the y-axis gathered from Screen().onclick()
    self.puzzle is a Puzzle class
    self.button is a list of Button class (reset, load, quit)
    self.moves represents the moves input by the player
    self.player represents the name of the player
    self.cur_moves represents the numeber of moves that player has moved so far
    self.moves_shower is a Turtle object that prints self.cur_moves in the window
    self.leaderboard is a LeaderBoard class
    self.set_position() is a function that updates self.x and self.y
    self.show_move() is a function that makes self.moves_shower print current moves
    self.check_win() is a function that checks if the player wins or loses the game
    self.load_new_puzzle() is a function that loads a new set of puzzle with the
    file name that the player inputs
    self.buttons_click() is a function that checks if the player clicks on the
    buttons, and also executes the function of the buttons
    self.effective_click() is a function that checks if the player clicks on the
    adjacent pieces to the blank pieces
    """
    def __init__(self, puzzle, buttons, moves, player,leaderboard):
        self.x = 1001
        self.y = 1001
        self.puzzle = puzzle
        self.buttons = buttons
        self.moves = moves
        self.player = player
        self.cur_moves = 0
        self.moves_shower = Turtle(visible=False)
        self.leaderboard = leaderboard
        self.show_move()

    def set_position(self, x, y): # to receive (x,y) from Screen().onclick()
        self.x = x
        self.y = y
        self.effective_click() # check if player clicks on the adjacent pieces
        self.buttons_click() # check if player clicks on the buttons

    def show_move(self): # print current moves
        self.moves_shower.clear() # clear previous status
        self.moves_shower.penup()
        self.moves_shower.setposition(-300, -350)
        self.moves_shower.write("Player Moves: " + str(self.cur_moves),
                                False, align="center",
                                font=("Arial", 25, "normal"))

    def check_win(self): # check if the player win
        correct_num = 1 # correct assigned number
        for i in range(int(self.puzzle.info[1][1])):
            if self.puzzle.puz[i].num != correct_num:
                break # break the loop if the assigned number is not correct
            else: # keep going through self.puzzle.puz
                # if all the assigned numbers is correct (player wins)
                if i == int(self.puzzle.info[1][1]) - 1:
                    # update the leaderboard
                    self.leaderboard.update_leaders(self.player, self.cur_moves)
                    win_msg = Turtle(visible=False) # winning message
                    win_msg.shape("Resources/winner.gif")
                    win_msg.st()
                    time.sleep(3)
                    credits = Turtle(visible=False) # credit picture
                    credits.shape("Resources/credits.gif")
                    credits.st()
                    exitonclick() # exit the game

            correct_num += 1 # update the correct assigned number

        if self.cur_moves >= self.moves: # player loses
            lose_msg = Turtle(visible=False)
            lose_msg.shape("Resources/Lose.gif")
            lose_msg.st()
            time.sleep(3)
            credits = Turtle(visible=False)
            credits.shape("Resources/credits.gif")
            credits.st()
            exitonclick()

    def load_new_puzzle(self): # load a new set of puzzle
        entries = os.scandir() # search the .puz files
        puz_files = []

        for i in entries:
            if ".puz" in i.name:
                puz_files.append(i.name)
            if len(puz_files) > 10: # when the .puz files are more than 10
                puz_files.pop() # pop out the 11th file
                file_warning = Turtle(visible=False) # warning message
                file_warning.shape("Resources/file_warning.gif")
                file_warning.st()
                time.sleep(3)
                file_warning.ht()
                break

        # create the string content for the pop-up window
        puz_files_text = "\n".join(puz_files[x] for x in range(len(puz_files)))

        puz_name = textinput("Load Puzzle", "Enter the name of the puzzle " +
                             "your wish to load. Choices are:\n" +
                             puz_files_text)
        lst = [] # to store the information gathered from .puz
        legit_pieces = [4, 9, 16] # valid number of puzzle pieces
        try:
            with open(puz_name, mode="r") as r_file:
                for i in r_file:
                    lst.append(i.strip().split(":"))
            if int(lst[1][1]) in legit_pieces: # number of puzzle pieces is valid
                self.puzzle.clear_all() # clear the previous set of puzzle
                self.puzzle.thumb_n.ht() # clear thumbnail picture
                self.puzzle = Puzzle(lst) # assign the new set of puzzle
                self.cur_moves = 0 # reset self.cur_moves
                self.show_move()
            else: # number of puzzle pieces is not valid
                error_msg = Turtle(visible=False) # error message
                error_msg.shape("Resources/file_error.gif")
                error_msg.st()
                time.sleep(3)
                error_msg.ht()
                with open("5001_puzzle.err", mode="a") as a_file: # update error log
                    dt = datetime.now()
                    cur = dt.strftime("%a, %b %d, %Y, %H:%M:%S ")
                    err_log = (cur + f"Error: File \"{puz_name}\" does not have " +
                               "valid number of puzzle pieces "
                               "LOCATION: Game.load_new_puzzle()\n")
                    a_file.write(err_log)

        except FileNotFoundError: # file is not found
            error_msg = Turtle(visible=False)
            error_msg.shape("Resources/file_error.gif")
            error_msg.st()
            time.sleep(3)
            error_msg.ht()
            with open("5001_puzzle.err", mode="a") as a_file: # update error log
                dt = datetime.now()
                cur = dt.strftime("%a, %b %d, %Y, %H:%M:%S ")
                err_log = (cur + f"Error: File \"{puz_name}\" does not exit " +
                           "LOCATION: Game.load_new_puzzle()\n")
                a_file.write(err_log)

    def buttons_click(self): # check if the player click on the buttons
        r_area = self.buttons[0].area # get the area [[x1, x2], [y1, y2]]
        l_area = self.buttons[1].area
        q_area = self.buttons[2].area

        # clicks on reset button
        if r_area[0][0] <= self.x <= r_area[0][1] and r_area[1][0] <= self.y <= r_area[1][1]:
            self.puzzle.clear_all()
            self.puzzle.reset()

        # clicks on load button
        if l_area[0][0] <= self.x <= l_area[0][1] and l_area[1][0] <= self.y <= l_area[1][1]:
            self.load_new_puzzle()

        # clicks on quit button
        if q_area[0][0] <= self.x <= q_area[0][1] and q_area[1][0] <= self.y <= q_area[1][1]:
            quit_m = Turtle(visible=False) # quit message
            quit_m.shape("Resources/quitmsg.gif")
            quit_m.st()
            time.sleep(3)
            credits = Turtle(visible=False)
            credits.shape("Resources/credits.gif")
            credits.st()
            exitonclick() # exit the game

    def effective_click(self): # check if the player clicks on the adjacent pieces
        for i in self.puzzle.e_pieces:
            area = self.puzzle.puz[i].area # get the area of each adjacent piece
            if area[0][0] <= self.x <= area[0][1] and area[1][0] <= self.y <= area[1][1]:
                # switch two Pieces classes in self.puzzle.puz
                self.puzzle.move_order(self.puzzle.blank, i)
                self.cur_moves += 1
                self.show_move()
                self.check_win() # check if the player wins

class Button(object):
    """
    This is a class to create buttons (reset, load, quit)
    self.position represents the button's position
    self.pic is the directory of the button picture
    self.size stores the width and height of the button picture [width, height]
    self.area stores the range of x-axis and y-axis of the button's area
    self.create_turtle() is a function that creates a Turtle object with the
    button picture and the given position
    self.set_area is a function that calculate the range of the button's area
    """
    def __init__(self, position, pic, size):
        self.position = position
        self.pic = pic
        self.size = size
        self.area = [0, 0]
        self.create_turtle()
        self.set_area()

    def create_turtle(self):
        self.tur = Turtle(visible=False)
        self.tur.shape(self.pic)
        self.tur.penup()
        self.tur.speed(10)
        self.tur.setposition(self.position[0], self.position[1])
        self.tur.st()

    def set_area(self):
        h_width = self.size[0] // 2
        h_height = self.size[1] // 2
        self.area[0] = [self.position[0] - h_width, self.position[0] + h_width]
        self.area[1] = [self.position[1] - h_height, self.position[1] + h_height]

def main():
    wn = Screen()
    entries = os.scandir("Resources/")
    for i in entries:
        # register all the pictures in Resources
        Screen().register_shape("Resources/" + i.name)


    setup(width = 1000, height = 1000)
    title("CS5001 Sliding Puzzle Game")
    splash_screen = Turtle(visible=False)
    splash_screen.shape("Resources/splash_screen.gif")
    splash_screen.st()
    time.sleep(2)
    splash_screen.ht()

    player_name = textinput("CS5001 Puzzle Slide",
                            "Your Name:") # get player's name
    moves = numinput("CS5001 Puzzle Slide - Moves",
                     "Enter the number of moves your want (5-200)",
                     100, minval=5, maxval=200) # get the number of moves that player wants

    frame1 = Frame(600, 520, [-425, 415]) # set main frames
    frame2 = Frame(600, 260, [150, 415])
    frame3 = Frame(120, 835, [-425, -280])
    frame1.paint() # print the frames
    frame2.paint("blue")
    frame3.paint()
    reset_b = Button([150, -340], "Resources/resetbutton.gif", [80, 80]) # set all buttons
    load_b = Button([250, -340], "Resources/loadbutton.gif", [80, 76])
    quit_b = Button([350, -340], "Resources/quitbutton.gif", [80, 53])
    buttons = [reset_b, load_b, quit_b] # store Button classes in a list

    lst = [] # to store the information of the default puzzle
    with open("mario.puz", mode="r") as r_file:
        for i in r_file:
            lst.append(i.strip().split(":"))

    puz1 = Puzzle(lst) # set the default puzzle
    lb = LeaderBoard() # set the leaderboard
    # set the game with all the classes we created
    game = Game(puz1, buttons, moves, player_name, lb)
    # passing (x,y) from onclick() method to game.set_position()
    wn.onclick(game.set_position)

    wn.mainloop()
if __name__ == "__main__":
    main()
