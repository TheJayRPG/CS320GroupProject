"""
Alexander Hong
CS 320
Experimental Grid

This is a Python based version of Conway's Game of Life used for quickly
testing features and experimenting with miscellaneous implementations.

While in the directory the program is stored in,
it can be run from the terminal by typing:
    python3 experGrid.py

Command prompts will be provided for user input.
"""

import time
import random

# Class used to store data on a rule
# Range indicates how far a cell detects other cells around it during updates
# Most is the maximum number of nearby cells required for being alive
# Least is the minimum number of nearby cell required for being alive
class Rule():
    def __init__(self, range, most, least):
        self.r = range #1
        self.m = most #3
        self.l = least #2

# Class used to store data on a cell's position and status
# xpos and ypos indicate the cell's position on a 2D grid
# status indicates being dead (0) or alive (1)
class Cell():
    def __init__(self, xpos, ypos, status):
        self.x = xpos
        self.y = ypos
        self.s = status

    # Toggles a cell from being dead to alive, or alive to dead
    def cellToggle(self):
        if self.s == 1:
            self.s = 0
        else:
            self.s = 1

# Class used to store the information of cell on a 2D grid
# Width and height are the dimensions of the grid
# self.grid is an array used to hold rows of cells
class CellGrid():
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.grid = []
        self.newGrid()

    # Creates a new grid full of dead cells
    def newGrid(self):
        self.grid = []
        for y in range(self.h):
            row = []
            for x in range(self.w):
                row.append(Cell(x, y, 0))
            self.grid.append(row)

    # Prints a visualization of the grid into the terminal
    def printGrid(self):
        for y in range(self.h):
            print("|", end = '')
            for x in range(self.w):
                if self.grid[y][x].s == 0:
                    print("_|", end = '')
                else:
                    print("0|", end = '')
            print()

    # Randomizes the cells on a grid given a probability out of 100
    def randomGrid(self, prob):
        for y in range(self.h):
            for x in range(self.w):
                chance = random.choice(range(100))
                if chance < prob:
                    self.grid[y][x].s = 1

    # Updates all the cells on a grid in accordance to a rule
    def updateGrid(self, rule):
        for y in range(self.h):
            for x in range(self.w):
                nearby = 0
                for j in range(rule.r + 1):
                    for i in range(rule.r + 1):
                        if j == 0 and i == 0:
                            continue
                        if y + j < self.h:
                            if x + i < self.w:
                                if self.grid[y + j][x + i].s == 1:
                                    nearby += 1
                            if x - i < self.w:
                                if self.grid[y + j][x - i].s == 1:
                                    nearby += 1
                        if y - j > -1:
                            if x + i < self.w and i > 0 and j > 0:
                                if self.grid[y - j][x + i].s == 1:
                                    nearby += 1
                            if x - i < self.w and i > 0 and j > 0:
                                if self.grid[y - j][x - i].s == 1:
                                    nearby += 1
                print("|" + str(nearby), end = '')
            print()

# Determines if a given input is a valid integer
def intValid(dim):
    result = 0
    while 1:
        try:
            result = int(dim)
            if result > 0:
                break
        except:
            pass
        dim = input("Enter a valid integer: ")
    return result

# Not yet utilized
def comInput():
    pass

# Currently performs a series of test functions:
# Prompts the user for grid dimensions
# Displays a randomized grid using the given dimensions
# Attempts to update the grid using CGoL default rules
# Displays commands to the user and prompts an input
def main():
    width = intValid(input("Enter grid width: "))
    height = intValid(input("Enter grid height: "))
    cGrid = CellGrid(width, height)

    cGrid.randomGrid(20)
    cGrid.printGrid()

    testRule = Rule(1, 3, 2)

    cGrid.updateGrid(testRule)

    while 1:
        print("Commands: quit|q, ")
        inp = input("Enter command: ")
        if inp == "quit" or inp == "q":
            break

if __name__=='__main__':
    main()
