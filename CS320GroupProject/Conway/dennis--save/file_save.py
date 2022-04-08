#Take the 4 objects(Rules, Status, Cell, Thoughts) necessary to re build a Conway's game of life and write their values to a file
#The objects refereed where created by Kristine Hess
def saveProgram(Rules,Status,Cell,Thoughts):
    #create a file named file and open it for writing
    try:
        file = open("file","w")
    except:
        print("error")
        return -1
    #Write all the values of the Rules object into the file and check for errors. Return -1 for and print
    try:
        file.write("Rules:")
    except:
        print("error")
        return -1
    try:
        file.write(str(Rules.shape))
    except:
        print("error")
        return -1
    try:
        file.write(str(Rules.pattern))
    except:
        print("error")
        return -1
    try:
        file.write(str(Rules.min2live))
    except:
        print("error")
        return -1
    try:
        file.write(str(Rules.max2live))
    except:
        print("error")
        return -1
    try:
        file.write(str(Rules.min2spawn))
    except:
        print("error")
        return -1
    try:
        file.write(str(Rules.max2spawn))
    except:
        print("error")
        return -1
    #write Generation to file to indicate a cutoff point for the Rules object and start writing to file for Status, the object that represents Generation
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
        return file
    

        
    
            
        
    

