from shutil import ReadError
from delete_lines_from_file import delete_lines_from_file
import unittest
def save_Cells_Environment(filename,Cell_Environment):
    try:
        file = open(filename,"a")
    except FileNotFoundError:
        print("error writing to file in save_cells_environment")
        file.close()
        raise
    file.write("Cell_Environment")
    file.write(str(Cell_Environment.gen2stable))
    file.write(str(Cell_Environment.period))
    file.write(str(Cell_Environment.stable))
    file.write("Living")
    for a in range(len(Cell_Environment.living)):
        file.write(str(Cell_Environment.living[a]))
    file.write(str(Cell_Environment.numLiving))
    file.write("Changed")
    for b in range(len(Cell_Environment.changed)):
        file.write(str(Cell_Environment.changed[b]))
    file.write(str(Cell_Environment.numChanged))
    return 0
def load_Save_Cell_Environment(filename,Cell_Environment):
    count = 8
    try:
        file = open(filename,"r")
    except FileNotFoundError:
        print("error opening file in load save cel environemnt")
        file.close()
        raise
    try:
        Cell_Environment.gen2stable = int(file.readline())
    except ReadError:
        print("Trouble reading in load save cell environment")
        file.close()
        raise
    Cell_Environment.period = int(file.readline())
    Cell_Environment.stable = int(file.readline())
    if(file.readline() == "Living"):
        for a in range(len(Cell_Environment.living)):
            Cell_Environment.living[a] = file.readline()
            count = count + 1
    Cell_Environment.stable = file.readline()
    if(file.readline() == "changed"):
        for a in range(len(Cell_Environment.changed)):
            Cell_Environment.changed[a] = file.readline()
            count = count + 1
    Cell_Environment.numChanged = file.readline()
    file.close()
    delete_lines_from_file()
    return 0
