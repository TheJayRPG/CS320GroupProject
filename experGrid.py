# Alexander Hong
# CS 320
# Experimental Grid

import time
import random

class Test():
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def show(self):
        print(self.x)
        print(self.y)

class Cell():
    def __init__(self, xpos, ypos, alive):
        self.x = xpos
        self.y = ypos
        self.a = alive

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
                print(str(self.grid[i][j].a) + "|", end = '')
            print()

def main():
    width = input("Enter grid width: ")
    height = input("Enter grid height ")

    test = CellGrid(width, height)
    test.printGrid()
    while True:
        inp = input("Enter input: ")
        print(inp)
        if inp == "end":
            break

if __name__=='__main__':
    main()
