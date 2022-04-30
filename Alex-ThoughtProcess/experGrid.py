"""
Alexander Hong
CS 320
https://github.com/TheJayRPG/CS320GroupProject
Custom Game of Life - Experimental Grid
experGrid.py

This is a Python based version of Conway's Game of Life used for quickly
testing features and experimenting with miscellaneous implementations.

While in the directory the program is stored in,
the program can be run from the terminal by typing:
    python3 experGrid.py

Command prompts will be provided for user input.
"""
import experRule
import time
import random


"""
Cell

Class used to store data on a cell's position and status.
    x           Integer representing the x position of the cell.
    y           Integer representing the y position of the cell.
    status      Integer indicating being dead (0) or alive (1).
"""
class Cell():
    def __init__(self, xpos, ypos, status):
        self.x = xpos
        self.y = ypos
        self.s = status

    """
    cellToggle

    Toggles a cell from being dead to alive, or alive to dead.
    """
    def cellToggle(self):
        if self.s == 1:
            self.s = 0
        else:
            self.s = 1

"""
CellGrid

Class used to store the information of cell on a 2D grid.
    w       Integer representing the width of the grid.
    h       Integer representing the height of the grid.
    grid    An array used to hold rows of cells.
"""
class CellGrid():
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.grid = []
        self.newGrid()

    """
    newGrid

    Creates a new grid full of dead cells.
    """
    def newGrid(self):
        self.grid = []
        for y in range(self.h):
            row = []
            for x in range(self.w):
                row.append(Cell(x, y, 0))
            self.grid.append(row)

    """
    printGrid

    Prints a visualization of the grid into the terminal.
    """
    def printGrid(self):
        for y in range(self.h):
            print("|", end = '')
            for x in range(self.w):
                if self.grid[y][x].s == 0:
                    print("_|", end = '')
                else:
                    print("0|", end = '')
            print()

    """
    randomGrid

    Randomizes the cells on a grid given a probability out of 100.
    """
    def randomGrid(self, prob):
        for y in range(self.h):
            for x in range(self.w):
                chance = random.choice(range(1, 101))
                if chance <= prob:
                    self.grid[y][x].s = 1

    """
    updateGrid

    Updates all the cells on a grid in accordance to a rule
    """
    def updateGrid(self, rule):
        temp = CellGrid(self.w, self.h)
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
                            if x - i > -1 and i > 0:
                                if self.grid[y + j][x - i].s == 1:
                                    nearby += 1
                        if y - j > -1:
                            if x + i < self.w and j > 0:
                                if self.grid[y - j][x + i].s == 1:
                                    nearby += 1
                            if x - i > -1 and i > 0 and j > 0:
                                if self.grid[y - j][x - i].s == 1:
                                    nearby += 1
                if nearby <= rule.m and nearby >= rule.l:
                        temp.grid[y][x].s = 1
        self.grid = temp.grid

        """
        updateGridD(self, rule)

        Updates all cells on, searching in a diamond pattern instead of square.
        """
        def updateGridD(self, rule):
            temp = CellGrid(self.w, self.h)
            for y in range(self.h):
                for x in range(self.w):
                    nearby = 0
                    for j in range(rule.r + 1):
                        for i in range(j + 1):
                            print("Reached j: " + str(j) + " i: " + str(i))
            self.grid = temp.grid

"""
intValid

Determines if a given input is a valid integer.
"""
def intValid(dim):
    result = 0
    while 1:
        try:
            result = int(dim)
            if result >= 0:
                break
        except:
            pass
        dim = input("Enter a valid integer: ")
    return result

"""
intValid2

Determines if a given input is valid with out using user input.
"""
def intValid2(dim):
    result = -1
    if type(dim) == int:
        print("Passed")
        result = dim
        if result < 0 or result >= 100:
            return -1
    return result

"""
comInput

Determines input commands
"""
def comInput(grid, rule):
    print("Commands: quit|q, next|n, rand|r, toggle|t, ")
    inp = input("Enter command: ")

    if inp == "next" or inp == "n":
        grid.updateGrid(rule)
        grid.printGrid()
        print()
        return grid

    if inp == "rand" or inp == "r":
        print("Probability of life needed...")
        prob = 0
        while 1:
            prob = input("Enter an integer between 0 and 100: ")
            prob = intValid(prob)
            if prob >= 0 and prob <= 100:
                break
        grid.randomGrid(prob)
        grid.printGrid()
        print()
        return grid

    if inp == "toggle" or inp == "t":
        print("Give the location of a cell...")
        xpos = 0
        ypos = 0
        while 1:
            xpos = input("Enter an X between 0 and " + str(grid.w) + ": ")
            xpos = intValid(xpos)
            if xpos >= 0 and xpos < grid.w:
                break
        while 1:
            ypos = input("Enter an Y between 0 and " + str(grid.h) + ": ")
            ypos = intValid(ypos)
            if ypos >= 0 and ypos < grid.h:
                break

        grid.grid[ypos][xpos].cellToggle()
        grid.printGrid()
        print()
        return grid

    if inp == "quit" or inp == "q":
        return 0

    else:
        return -1

"""
main

Currently performs a series of test functions:
Prompts the user for grid dimensions
Displays a randomized grid using the given dimensions
Attempts to update the grid using CGoL default rules
Displays commands to the user and prompts an input
"""
def main():
    width = intValid(input("Enter grid width: "))
    height = intValid(input("Enter grid height: "))
    cGrid = CellGrid(width, height)

    cGrid.printGrid()
    print()
    testRule = experRule.Rule(1, 3, 2)

    while 1:
        inp = comInput(cGrid, testRule)
        if type(inp) == int and inp == 0:
            break


if __name__=='__main__':
    main()
