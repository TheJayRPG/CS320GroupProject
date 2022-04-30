"""
Alexander Hong
CS 320
https://github.com/TheJayRPG/CS320GroupProject
Custom Game of Life - Cell Thought Process
cellTPView.py

This file is used to print the information held in cellTP.py classes.
Primarily used for examining the outcomes of the cellTP methods.
"""

import cellTP

"""
showCellView

Prints the data held within a given cell to the terminal.
"""
def showCellView(cell):
    print("---Cell Info---")
    print(cell.strInfo())
    print("  --History Info-- [" + str(cell.historySize()) + "]")
    print(cell.historyInfo())

"""
showLogView

Prints the data held within a given log to the terminal.
"""
def showLogView(log):
    print("-Log Info-")
    print(log.strInfo())

"""
showHistoryView

Prints the log data held within the history object.
"""
def showHistoryView(history):
    print("--History Info--")
    print(history.strInfo() + "\n")

"""
main

Executes demonstration of view methods in terminal.
"""
def main():
    history = None
    cell1 = cellTP.TPCell(5, 5, 10, 0, 8, 3, 5, history)
    log1 = cellTP.Log(cell1)
    history = cellTP.History(log1)
    cell2 = cellTP.TPCell(5, 5, 11, 1, 8, 6, 2, history)
    log2 = cellTP.Log(cell2)
    history.updateRecent(log2)
    cell3 = cellTP.TPCell(5, 5, 12, 0, 8, 0, 8, history)
    log3 = cellTP.Log(cell3)
    history.updateRecent(log3)

    showCellView(cell1)
    showCellView(cell2)
    showCellView(cell3)
    showLogView(log1)
    showLogView(log2)
    showLogView(log3)
    showHistoryView(history)

if __name__=='__main__':
    main()
