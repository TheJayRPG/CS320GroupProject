# Alexander Hong
# CS 320
# Experimental Grid

import time
import random

class Rule():
    def __init__(self, range, most, least):
        self.r = 1
        self.m = 3
        self.l = 2

class Cell():
    def __init__(self, xpos, ypos, status):
        self.x = xpos
        self.y = ypos
        self.s = status

    def cellToggle(self):
        if self.s == 1:
            self.s = 0
        else:
            self.s = 1

class CellGrid():
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.grid = []
        self.newGrid()

    def newGrid(self):
        self.grid = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(Cell(j, i, 0))
            self.grid.append(row)

    def printGrid(self):
        for i in range(self.h):
            print("|", end = '')
            for j in range(self.w):
                if self.grid[i][j].s == 0:
                    print("_|", end = '')
                else:
                    print("0|", end = '')
            print()

    def randomGrid(self, prob):
        for i in range(self.h):
            for j in range(self.w):
                chance = random.choice(range(100))
                if chance < prob:
                    self.grid[i][j].s = 1

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

def comInput():
    pass

def main():
    width = intValid(input("Enter grid width: "))
    height = intValid(input("Enter grid height: "))
    cGrid = CellGrid(width, height)

    cGrid.randomGrid(40)

    cGrid.printGrid()

    while 1:
        print("Commands: quit|q, ")
        inp = input("Enter command: ")
        if inp == "quit" or inp == "q":
            break

if __name__=='__main__':
    main()
