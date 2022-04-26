def delete_lines_from_file(filename,count):
    with open(filename,"r") as file:
        list = file.readlines()
    file.close()
    with open(filename,"w") as file:
        for line in list:
            count = count -1
            if(count == 0):
                file.write(line)
    file.close()
            
        

