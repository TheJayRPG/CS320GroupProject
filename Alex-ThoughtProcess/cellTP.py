"""
Alexander Hong
CS 320
https://github.com/TheJayRPG/CS320GroupProject
Custom Game of Life - Cell Thought Process
cellTP.py

This file provides the classes used to store information on a selected cell's
changes and the observations it makes to surrounding cells.
To be used from main.py via import.
For examining method results, import into cellTPView.py
"""

"""
TPCell

Class that stores the relevant data of a selected cell.
    xPos        Integer representing the y position of the cell.
    yPos        Integer representing the y position of the cell.
    age         Integer representing the current lifecycle the cell is on.
    status      Integer representing if a cell if dead(0) or alive(1).
    nearby      Integer representing the number of surrounding cells.
    liveNear    Integer representing the number of nearby living cells.
    deadNear    Integer representing the number of nearby dead cells.
    history     History of the 10 most recent history Logs for the cell.
"""
class TPCell():
    def __init__(self, x, y, a, s, n, ln, dn, h):
        self.xPos = x
        self.yPos = y
        self.age = a
        self.status = s
        self.nearby = n
        self.liveNear = ln
        self.deadNear = dn
        self.history = h

    """
    strInfo

    Returns the information in the cell in a string format.
    """
    def strInfo(self):
        cellInfo = ""
        cellInfo += "  [" + str(self.xPos) + ", " + str(self.yPos) + "]\n"
        cellInfo += "  Age: " + str(self.age) + "\n"
        cellInfo += "  Nearby: " + str(self.nearby) + "\n"
        cellInfo += "  Living: " + str(self.liveNear) + "\n"
        cellInfo += "  Dead: " + str(self.deadNear) + "\n"
        statDict = {0: "Dead", 1: "Live"}
        cellInfo += "  Status: " + statDict.get(self.status, "Other")
        return cellInfo

    """
    historySize

    Returns the size of the history object stored.
    """
    def historySize(self):
        if self.history != None:
            return self.history.getSize()

    """
    historyInfo

    Returns the history object's info as a string.
    """
    def historyInfo(self):
        if self.history != None:
            return self.history.strInfo()
        else:
            return "    Nothing in history\n"

"""
Log

Class that stores the information on the changes to be made for a TPCell.
Performs like a linked list, refering to previous entries for the cell.
    age         Integer representing the current lifecycle the cell is on.
    status      Integer representing the number of surrounding cells.
    nearby      Integer representing the number of surrounding cells.
    liveNear    Integer representing the number of nearby living cells.
    deadNear    Integer representing the number of nearby dead cells.
    change      Indicates if this log's status is different from the previous
"""
class Log():
    def __init__(self, cell):
        self.age = cell.age
        self.status = cell.status
        self.nearby = cell.nearby
        self.liveNear = cell.liveNear
        self.deadNear = cell.deadNear
        self.prev = None
        self.change = False

    """
    changeCheck

    Checks if the previous log had a different state (alive or dead) and
    toggles the change variable to True.
    """
    def changeCheck(self):
        if self.prev != None and self.prev.status != self.status:
            self.change = True

    """
    strInfo

    Provides a simplified version of the log info in string format.
    """
    def strInfo(self):
        logInfo = "  ["
        logInfo += str(self.age) + "]"
        logInfo += " N: " + str(self.nearby)
        logInfo += " L: " + str(self.liveNear)
        logInfo += " D: " + str(self.deadNear)
        statDict = {0: " Dead", 1: " Live"}
        logInfo += statDict.get(self.status, "Other")
        if self.prev != None:
            logInfo += " > [" + str(self.prev.age) + "]"
        if self.change != False:
            logInfo += " CHANGE"
        logInfo += "\n"
        return logInfo

"""
History

Class used for recording the throught process history of a cell using logs.
Holds the 10 most recent logs of a cell.
"""
class History():
    def __init__(self, recentLog):
        self.size = 1
        self.recent = recentLog
        self.record = [recentLog]

    """
    getSize

    Returns the size of the History object.
    """
    def getSize(self):
        return self.size

    """
    updateRecord

    Recreates the history record by iterating through the 10 most recent logs.
    """
    def updateRecord(self):
        log = self.recent
        log.changeCheck()
        newRecord = []
        for a in range(10):
            newRecord.append(log)
            if log.prev == None:
                break
            else:
                log = log.prev
        self.record = newRecord

    """
    updateRecent

    Tells the history object to update itself with the provided new log.
    """
    def updateRecent(self, newLog):
        newLog.prev = self.recent
        self.recent = newLog
        if self.size < 10:
            self.size += 1
        self.updateRecord()

    """
    strInfo

    Provides a string version of each log in the record array.
    """
    def strInfo(self):
        hisInfo = ""
        for log in self.record:
            hisInfo += "  " + log.strInfo()
        return hisInfo

"""
recordCell

Given the x and y positions of an array of cells, begins recording
logs of the cell's history.
Returns a version of the cell with a history object set to self.history.
"""
def recordCell(x, y, cellArray):
    cell = cellArray[y][x]
    cellLog = Log(cell)
    cell.history = History(cellLog)

    return cell

