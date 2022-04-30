from io import RawIOBase
from msilib.schema import File
from shutil import ReadError
from tokenize import String
import unittest
from venv import create
from delete_lines_from_file import delete_lines_from_file
from create_file_name import create_file_name
"""rulesWrite takes the inputs of a string filename and the Rules Object and writes the values inside Rules to a file for saving. Returns a 0 for success"""
def rulesWrite(filename : String,Rules):
    #try to open filename. If file is not found, raise the FileNotFoundError and close the file
    try:
        file = open(filename,"a")
    except FileNotFoundError:
        file.close()
        print("Error in rulesWrite")
        raise
    #Write all the values of the Rules object into the file
    file.write("Rules:")
    file.write(str(Rules.rows))
    file.write(str(Rules.columns))
    file.write(str(Rules.shape))
    file.write(str(Rules.pattern))
    file.write(str(Rules.min2live))
    file.write(str(Rules.max2live))
    file.write(str(Rules.min2spawn))
    file.write(str(Rules.max2spawn))
    #close the file and return 0 to signify success
    file.close()
    return 0



"""statusWrite takes the inputs of a string filename and the Status Object and writes the values inside Rules to a file for saving. Returns a 0 for success"""
def statusWrite(filename,Status):
    #try to open filename. If file is not found, raise the FileNotFoundError and close the file
    try:
        file = open(filename,"a")
    except FileNotFoundError:
        file.close()
        print("error")
        raise
    file.write("Generation")
    #write the elements of the 2d Status array object to the file
    for a in Status:
        file.write("Row " + str(a))
        for b in range(len(a)):
            file.write(str(a[b]))  
    #close the file and return 0 for success
    file.close()
    return 0



"""cellWrite takes the inputs of a string filename and the Cell Object and writes the values inside Rules to a file for saving. Returns a 0 for success"""
def cellWrite(filename, Cell):
    #try to open filename. If fail, raise FileNotFoundError and close the file
    try:
        file = open(filename,"a")
    except FileNotFoundError:
        file.close()
        print("error in CellWrite opening file")
        raise
    file.write("Stats")
    #write the elements and attributes of the 2d array element Cell
    for c in Cell:
        file.write("Row " + str(c))
        for d in c:
            print("Type is " + str(type(d)))
            file.write("Cell " + str(d) + " Stats")
            file.write("Neighbors " + str(d.neighbors))
            for e in d.past:
                print("Type is" + str(type(e)))
                file.write(str(d.past[e]))
            file.write("Generations " + str(d.generations))
            file.write(str(d.living))
            file.write(str(d.dead))
            file.write(str(d.stableAt))
        #close the file and return 0 for success
        file.close()
        return 0




"""To save all the values needed to restore a version of Conways game, take the writeFile paramaters Rules, Status and Cell and write their elements to filename. Returns a 0 for success, -1 for failure"""
def writeFile(filename,Rules, Status, Cell):
    #if filename is an empty string, create a new filename in the filename function
    if filename ==  " ":
        filename = create_file_name(0,1)
    #make sure the write functions for the Rules, Status and Cells objects succeed. If all succeed return 0 for success, if at least one fails, return -1 for fail
    if(rulesWrite(filename,Rules) == 0):
        if(statusWrite(filename,Status)) == 0:
            if cellWrite(filename, Cell) == 0:
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1




"""loadRules takes fileName and opens it to read its values to the Object Rules. Returns -1 for fail,0 for success and raise error for errors"""
def loadRules(fileName,Rules):
    #there will 9 lines read in this function. Afterwards this same number of lines must be deleted
    line_count = 9
    #try to open filename as file for reading. If file not found, rise FileNotFoundError and close the file
    try:
        file = open(fileName,"r")
    except FileNotFoundError:
        print("error")
        file.close()
        raise
    #check if the line in the file is "Rules" to start load state. Otherwise, print error,close file and raise ReadError 
    try:
        checkIfRules = str(file.readline())
    except ReadError:
        print("eror writing in loadRules")
        file.close()
        raise
    #check if one line is "Rules" in filename. It is a line for debugging and has no effect on the game state. If line is not Rules, return -1 for wrong file
    if(checkIfRules == "Rules:"): 
        #Read and initiliaze the values in the Rules object given the file.
        try:
            Rules.rows = int(file.readline())
        except ReadError:
            print("Error reading file or error with type system")
            file.close()
            raise
        Rules.columns = int(file.readline())
        Rules.shape = int(file.readline())
        Rules.pattern = int(file.readline())
        Rules.min2live = int(file.readline())
        Rules.max2live = int(file.readline())
        Rules.min2spawn = int(file.readline())
        Rules.max2spawn = int(file.readline())
        file.close()
        #delete line_count amount lines from fileName to make sure that the lines read are not read again
        delete_lines_from_file(fileName,line_count)
        #return 0 for success
        return 0
    else:
        #always close the file when exiting
        file.close()
        return -1





"""loadGeneration takes fileName and opens it to read its values to the Generation Rules. Returns -1 for fail,0 for success and raise error for errors"""
def loadGeneration(fileName,CellGeneration):
    #try to open filename as file for reading. Raise FileNotFoundError if error occurs
    line_count = 1
    try:
        file = open(fileName,"r")
    except FileNotFoundError:
        print("error opening file in loadGeneration")
        raise
    #check to see if line is debug line "Generation". If so skip line and continue. else close file and return -1 for fail
    if(str(file.readline()) == "Generation:"):
         #This line of code was created by Kristine Hess. was used for initializing here
        CellGeneration = [[0] * COLUMNS for _ in range(ROWS)]
        #Loop through cell generations until new segment for Stats is reached and add all the attributes necessary from the file reading.
        while(str(file.readline()) != "Stats"):
            for a in range(len(CellGeneration)):
                file.readline()
                for b in range(len(CellGeneration[a])):
                    CellGeneration[a][b].status = int(file.readline())
        #return 0 for success and before close the file. Also delete the lines previously read in delete lines from file
        file.close()
        delete_lines_from_file(fileName,line_count)
        return 0
    else:
        file.close()
        return -1




"""loadStatus takes fileName and opens it to read its values to the Object Status. Returns -1 for fail,0 for success and raise error for errors"""
def loadStatus(fileName,Status):
    #since the number of lines here is variable, start line_count at 0
    line_count = 0
    #try to open fileName as file for reading. If faile print error message, close file and raise FileNotFoundError
    try:
        file = open(fileName,"r")
    except FileNotFoundError:
        print("error in loadStatus")
        file.close()
        raise
    #For each element in Status increase line count for debug line you should not care about and loop the array c in Statis
    for c in Status:
        file.readline()
        line_count = line_count + 1
        print(type(c))
        #for each element d in the cth element of the Status object, fill up the Status object with relevant values
        for d in range(len(Status[c])):
            Status[c][d].neigbors = int(file.readline())
            Status[c][d].generations = int(file.readline())  
            Status[c][d].living = int(file.readline())                   
            Status[c][d].dead = int(file.readline())
            line_count = line_count + 4
    #close the file and delete the relevant lines from the file in fileName. return 0 for success
    file.close()
    delete_lines_from_file(fileName,line_count)
    return 0





"""To load all the values needed to restore a version of Conways game, take the file filename and read all its values to the objects Rules, Generation and Status. Returns a 0 for success, -1 for failure"""
def loadGame(filename,Rules, Generation, Status):
    #make sure the read functions for the Rules, Status and Cells objects succeed. If all succeed return 0 for success, if at least one fails, return -1 for fail
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






#tests
class TestOne(unittest.TestCase):
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
        result = cellWrite("file",cellStats)
        self.assertRaises(FileNotFoundError,result)
    #function coverage 
    def test_file_open_four(self):
        result = writeFile("file",rules,currentGeneration,cellStats)
        self.assertEquals(result,0)
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
    def test_file_load_six(self):
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
unittest.main()