# Alexander Hong
# CS 320
# Experimental Grid

import time
import random

class Cell():
    def __init__(self, xpos, ypos, alive):
        self.x = xpos
        self.y = ypos
        self.a = alive

    def cellToggle(self):
        if self.a == 1:
            self.a = 0
        else:
            self.a = 1

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

def main():
    width = intValid(input("Enter grid width: "))
    height = intValid(input("Enter grid height: "))
    cGrid = CellGrid(width, height)
    cGrid.printGrid()

    while 1:
        print("Commands: quit")
        inp = input("Enter command: ")
        if inp == "quit":
            break

if __name__=='__main__':
    main()
