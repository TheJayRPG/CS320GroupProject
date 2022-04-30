def create_file_name(shape, occurence):
    if(shape == 3):
        filename = "triangle" + "_" + str(occurence)
        return filename
    elif(shape == 4):
        filename = "square" + "_" + str(occurence)
        return filename
    elif(shape == 5):
        filename = "pentagon" + "_" + str(occurence)
        return filename
    elif(shape == 6):
        filename = "hexagon" + "_" + str(occurence)
        return filename
    else:
        filename = "file_" + str(occurence)
        return filename


