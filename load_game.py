#take a file and some important presumably constructed classes and fill those classes up with the data from the save file. return -1 on failure
#.main refers to group member Kristine Hess's file
from .main import ROWS, COLUMNS, Cell
def load_save(fileName, Rules, CellGeneration, Status):
    #open the input file given by FileName for reading as file and check for errors
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
            #loop through Status and add values to the Status object from values read from the file. Return -1 and print for errors
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
                    except:
                        print("error")
                        return -1
        #close file, print error and return -1 after failing to get proper line with "Stats"
        else:
            file.close()
            print("error")
            return -1
        #close file after success
        file.close()
    #if file is not appropriate for loading, close file, print error message and return -1
    else:
        file.close()
        print("Invalid save file")
        return -1

    

