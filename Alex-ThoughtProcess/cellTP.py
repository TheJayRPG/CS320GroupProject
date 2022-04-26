"""
Alexander Hong
CS 320
Cell Thought Process

This file is used to track the changes made by a selected cell.

To be used from main.py via import.
"""
import main

"""
Log

Class that stores the information on the changes to be made for a cell.
Performs like a linked list, refering to previous entries for the cell.

printLog
Displays the information held in a log for testing purposes.
"""
class Log():
    def __init__(self, cell):
        self.nearby = cell.neighbors
        self.living = cell.living
        self.dead = cell.dead
        self.gen = cell.generation
        self.state = ""
        self.prev = None
        self.change = False

    def changeCheck(self):
        pass

    def printLog(self):
        print("Nearby: " + str(self.nearby))
        print("Living: " + str(self.living))
        print("Dead: " + str(self.dead))
        print("Gen: " + str(self.gen))
        if self.prev != None:
            print("Prev: Exists")
        else:
            print("Prev: None")
        print("Change: " + str(self.change))

"""
History

Class used for recording the throught process history of a cell using logs.
Holds the 10 most recent logs of a cell.

updateRecord
Recreates the history record by iterating through the 10 most recent logs.

updateRecent
Tells the history object to update itself with the provided new log.

getString
Returns a string interpretation of the history object.

printHistory
Displays the log info held in the history object for testing purposes.
"""
class History():
    def __init__(self, recentLog):
        self.recent = recentLog
        self.record = [recentLog]

    def updateRecord():
        log = self.recent
        newRecord = []
        for a in range(10):
            newRecord.append(log)
            if log.prev == None:
                break
            else:
                log = log.prev
        self.record = newRecord

    def updateRecent(self, newLog):
        newLog.prev = self.recent
        self.recent = newLog
        updateRecord()

    def getString():
        strVer = ""
        for a in range(10):
            strVer += "[" + str(self.record[a].gen) + "] "
            strVer += "L: " + str(self.record[a].living) + " "
            strVer += "D: " + str(self.record[a].dead) + " "
            strVer += self.record[a].state
            if (self.record[a].chane == True):
                strVer += " CHANGE"
        return strVer

    def printHistory():
        for a in range(10):
            pass

"""
recordCell

Given the x and y positions of an array of cells, begins recording
logs of the cell's history.
Returns a version of the cell with a history object set to self.past
"""
def recordCell(xPos, yPos, cellArray):
    cell = cellArray[yPos][xPos]
    cellLog = Log(cell)
    cell.past = History(cellLog)

    return cell

"""
main

Used for testing the classes and methods in cellTP.py independently.
Currently unimplemented.
"""
def main():
    pass

if __name__=='__main__':
    main()
