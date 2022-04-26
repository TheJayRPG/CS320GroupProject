from io import RawIOBase
from msilib.schema import File
from shutil import ReadError
from tokenize import String
import unittest
from venv import create
import json
from delete_lines_from_file import delete_lines_from_file
from cell_env_save_load import save_Cells_Environment
from cell_env_save_load import load_Save_Cell_Environment
from create_file_name import create_file_name
def rulesWrite(filename : String,Rules):
    try:
        file = open(filename,"a")
    except FileNotFoundError:
        file.close()
        print("error")
        raise
    #Write all the values of the Rules object into the file and check for errors. Return -1 for and print
    file.write("Rules:")
    file.write(str(Rules.shape))
    file.write(str(Rules.pattern))
    file.write(str(Rules.min2live))
    file.write(str(Rules.max2live))
    file.write(str(Rules.min2spawn))
    file.write(str(Rules.max2spawn))
    file.close()
    return 0
def statusWrite(filename,Status):
    try:
        file = open(filename,"a")
    except FileNotFoundError:
        file.close()
        print("error")
        raise
    file.write("Generation")
    #write the elements of the 2d Status array object to the file and check for errors
    for a in Status:
        file.write("Row " + str(a))
        for b in range(len(a)):
            file.write(str(a[b]))  
    file.close()
    return 0
def cellWrite(filename, Status, Cell):
    try:
        file = open(filename,"a")
    except FileNotFoundError:
        file.close()
        print("error")
        raise
    file.write("Stats")
    #write the elements and attributes of the 2d array element Cell and check for errors
    for c in Cell:
        file.write("Row " + str(c))
        for d in c:
            print("Type is " + str(type(d)))
            file.write("Cell " + str(d) + " Stats")
            file.write("Neighbors " + str(d.neighbors))
            for e in d.past:
                print("Type is" + str(type(e)))
                #file.write(str(Cell[d].past[e]))
            file.write("Generations " + str(d.generations))
            file.write(str(d.living))
            file.write(str(d.dead))
            file.write(str(d.stableAt))
        #close the file and return it
        file.close()
        return 0
def writeFile(filename,Rules, Status, Cell):
    if filename ==  " ":
        filename = create_file_name(0,1)
    if(rulesWrite(filename,Rules) == 0):
        if(statusWrite(filename,Status)) == 0:
            if cellWrite(filename, Status, Cell) == 0:
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
def loadRules(fileName,Rules):
    line_count = 6
    try:
        file = open(fileName,"r")
    except FileNotFoundError:
        print("error")
        file.close()
        raise
    #check if the line in the file is "Rules" to start load state. Otherwise, print error and return -1
    try:
        checkIfRules = str(file.readline())
    except ReadError:
        print("eror writing in loadRules")
        file.close()
        raise
    if(checkIfRules == "Rules:"): 
        #Read and initiliaze the values in the Rules object given the file. return -1 for errors
        try:
            Rules.shape = int(file.readline())
        except ReadError:
            print("Error reading file or error with type system")
            file.close()
            raise
        Rules.min2live = int(file.readline())
        Rules.max2live = int(file.readline())
        Rules.min2spawn = int(file.readline())
        Rules.max2spawn = int(file.readline())
        delete_lines_from_file(fileName,line_count)
        #check if the next line to be read is Generation. If so start adding values to CellGeneration
        file.close()
        return 0
    else:
        return -1
def loadGeneration(fileName,CellGeneration):
    try:
        file = open(fileName,"r")
    except FileNotFoundError:
        print("error")
        raise
    checkIfCell = str(file.readline())
    if(checkIfCell == "Generation:"):
         #This line of code was created by Kristine Hess. was used for initializing here
        CellGeneration = [[0] * COLUMNS for _ in range(ROWS)]
            #Loop through cell generations until new segment for Stats is reached and add all the attributes necessary from the file reading. Return -1 for errors
        while(str(file.readline()) != "Stats"):
            for a in range(len(CellGeneration)):
                file.readline()
                for b in range(len(CellGeneration[a])):
                    CellGeneration[a][b] = int(file.readline())
        file.close()
        return 0
    else:
        file.close()
        return -1
def loadStatus(fileName,Status):
    line_count = 0
    try:
        file = open(fileName,"r")
    except:
        print("error")
        return -1
    for c in Status:
        file.readline()
        line_count = line_count + 1
        print(type(c))
        """for d in range(len(Status[c])):
            Status[c][d].neigbors = int(file.readline())
            Status[c][d].generations = int(file.readline())  
            Status[c][d].living = int(file.readline())                   
            Status[c][d].dead = int(file.readline())
            line_count = line_count + 4 """
    delete_lines_from_file(fileName,line_count)
    return 0
def loadGame(filename,Rules, Generation, Status):
    if loadRules(filename,Rules) == 0:
        if loadGeneration(filename,Generation) == 0:
            if loadStatus(filename,Status) == 0:
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1

"""class TestOne(unittest.TestCase):
    #acceptance test
    def test_file_open_one(self):
        file = create_file_name(0,1)
        result = rulesWrite("file",rules)
        self.assertRaises(FileNotFoundError,result)
    #acceptance test
    def test_file_open_two(self):
        file = create_file_name(0,1)
        result = statusWrite("file",currentGeneration)
        self.assertRaises(FileNotFoundError,result)
    #acceptance test
    def test_file_open_three(self):
        file = create_file_name(0,1)
        result = cellWrite("file",currentGeneration,cellStats)
        self.assertRaises(FileNotFoundError,result)
    #function coverage 
    def test_file_open_four(self):
        result = writeFile("file",rules,currentGeneration,cellStats)
        self.assertEquals(result,0) """
class Test(unittest.TestCase):
    #acceptance test
    def test_file_load_one(self):
        result = loadRules("file",rules)
        self.assertRaises(ReadError,result)
    #acceptance test
    def test_file_load_two(self):
        result = loadGeneration("file",cellStats)
        self.assertRaises(FileNotFoundError,result)
    #acceptance test
    def test_file_load_three(self):
        result = loadStatus("file",currentGeneration)
        self.assertEquals(result,0)
#function coverage
    def test_file_load_four(self):
        result = loadGame("file",rules,cellStats,currentGeneration)
        self.assertEquals(result,0) 
    #integration test
    def test_file_load_five(self):
        writeFile("file",rules,currentGeneration,cellStats)
        result = loadGame("file",rules,cellStats,currentGeneration)
        self.assertEquals(result,0)
    #acceptance test
    """def test_file_load_six(self):
        result = _get_neighbor_type(self,10,20,3)
        self.assertNotEquals(result,-1)
    #acceptance test
    def test_file_load_seven(self):
        result = _get_neighbor_type(self,10,20,4)
        self.assertNotEquals(result,-1)
    #acceptance test
    def test_file_load_eight(self):
        result = _get_neighbor_type(self,4,5,6)
        self.assertNotEquals(result,-1)
    """
unittest.main()