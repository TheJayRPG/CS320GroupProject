from email.errors import StartBoundaryNotFoundDefect
import unittest
import json
def rulesWrite(Rules):
    try:
        file = open("fileName","r")
    except:
        print("error")
        return -1
    checkIfRules = str(file.readline())
    if(checkIfRules == "Rules:"): 
        #Read and initiliaze the values in the Rules object given the file. return -1 for errors
        try:
            Rules.shape = int(file.readline())
        except:
            print("Error reading file or error with type system")
            return -1
        try:
            Rules.pattern = int(file.readline())
        except:
            print("error")
            return -1
        try:
            Rules.min2live = int(file.readline())
        except:
            print("error")
            return -1
        try:
            Rules.max2live = int(file.readline())
        except:
            print("error")
            return -1
        try:
            Rules.min2spawn = int(file.readline())
        except:
            print("error")
            return -1
        try:
            Rules.max2spawn = int(file.readline())
        except:
            print("error")
        file.close()
        return 0
    else:
        return -1
def statusWrite(Status):
    try:
        file = open("file","w")
    except:
        print("error")
        return -1
    try:
        file.write("Generation")
    except:
        print("error")
        return -1
    #write the elements of the 2d Status array object to the file and check for errors
    for a in Status:
        try:
            file.write("Row " + str(a))
        except:
            print("error")
            return -1
        for b in range(len(Status[a])):
            try:
                file.write(str(Status[a][b]))  
            except:
                print("Error opening file")
                return -1
    file.close()
    return 0
def cellWrite(Status, Cell):
    try:
        file = open("file","w")
    except:
        print("error")
        return -1
    try:
        file.write("Stats")
    except:
        print("error")
        return -1
    #write the elements and attributes of the 2d array element Cell and check for errors
    for c in Cell:
        try:
            file.write("Row " + str(c))
        except:
            print("error")
            return -1
        for d in Cell[c]:
            try:
                file.write("Cell " + str(d) + " Stats")
            except:
                print("error")
                return -1
            try:
                file.write("Neighbors " + str(Status[d].neighbors))
            except:
                print("error")
                return -1
            try:
                file.write(str("Generations " + Status[d].generations))
            except:
                print("error")
                return -1
            try:
                file.write(str(Status[d].living))
            except:
                print("error")
                return -1
            try:
                file.write(str(Status[d].living))
            except:
                print("error")
                return -1
        #close the file and return it
        file.close()
        return 0
def writeFile(Rules, Status, Cell):
    if(rulesWrite(Rules) == 0):
        if(statusWrite(Status)) == 0:
            if cellWrite(Status, Cell) == 0:
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1
    
def loadRules(fileName,Rules):
    try:
        file = open(fileName,"r")
    except:
        print("error")
        return -1
    #check if the line in the file is "Rules" to start load state. Otherwise, print error and return -1
    checkIfRules = str(file.readline())
    if(checkIfRules == "Rules:"): 
        #Read and initiliaze the values in the Rules object given the file. return -1 for errors
        try:
            Rules.shape = int(file.readline())
        except:
            print("Error reading file or error with type system")
            return -1
        try:
            Rules.pattern = int(file.readline())
        except:
            print("error")
            return -1
        try:
            Rules.min2live = int(file.readline())
        except:
            print("error")
            return -1
        try:
            Rules.max2live = int(file.readline())
        except:
            print("error")
            return -1
        try:
            Rules.min2spawn = int(file.readline())
        except:
            print("error")
            return -1
        try:
            Rules.max2spawn = int(file.readline())
        except:
            print("error")
            return -1
        #check if the next line to be read is Generation. If so start adding values to CellGeneration
        file.close()
    else:
        return -1
def loadGeneration(fileName,Generation):
    try:
        file = open(fileName,"r")
    except:
        print("error")
        return -1
    checkIfCell = str(file.readline())
    if(checkIfCell == "Generation:"):
         #This line of code was created by Kristine Hess. was used for initializing here
        CellGeneration = [[0] * COLUMNS for _ in range(ROWS)]
            #Loop through cell generations until new segment for Stats is reached and add all the attributes necessary from the file reading. Return -1 for errors
        while(str(file.readline()) != "Stats"):
            for a in range(len(CellGeneration)):
                file.readline()
                for b in range(len(CellGeneration[a])):
                    try:
                        CellGeneration[a][b] = int(file.readline())
                    except:
                        print("error")
                        return -1
        file.close()
        return 0
    else:
        file.close()
        return -1
def loadStatus(fileName,Status):
    try:
        file = open(fileName,"r")
    except:
        print("error")
        return -1
    for c in range(len(Status)):
        file.readline()
        for d in range(len(Status[c])):
            try:
                Status[c][d].neigbors = int(file.readline())
            except:
                print("error")
                return -1
            try:
                Status[c][d].generations = int(file.readline())  
            except:
                print("error")
                return -1 
            try:
                Status[c][d].living = int(file.readline())                   
            except:
                print("error")
                return -1
            try:
                Status[c][d].dead = int(file.readline())
                return 0
            except:
                print("error")
                return -1
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
class TestOne(unittest.TestCase):
    #acceptance test
    def test_file_open_one(self):
        result = rulesWrite(Rules)
        self.assertEquals(result,0)
    #acceptance test
    def test_file_open_two(self):
        result = statusWrite(Status)
        self.assertEquals(result,0)
    #acceptance test
    def test_file_open_three(self):
        result = cellWrite(Status,Cell)
        self.assertEquals(result,0)
    #function coverage 
    def test_file_open_four(self):
        result = writeFile(Rules,Status,Cell)
        self.assertEquals(result,0)
class Test(unittest.TestCase):
    #acceptance test
    def test_file_load_one(self):
        result = loadRules("file",Rules)
        self.assertEquals(result,0)
    #acceptance test
    def test_file_load_two(self):
        result = loadGeneration("file",CellGeneration)
        self.assertEquals(result,0)
    #acceptance test
    def test_file_load_three(self):
        result = loadStatus("file",Status)
        self.assertEquals(result,0)
    #function coverage
    def test_file_load_four(self):
        result = loadGame("file",Rules,CellGeneration,Status)
        self.assertEquals(result,0) 
    #integration test
    def test_file_load_five(self):
        writeFile(Rules,CellGeneration, Status)
        result = loadGame("file",Rules,CellGeneration,Status)
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