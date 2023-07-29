## prog5,6
## Jun 25
## Tony Lee
##

# prog 5

def boardermaker(grid):
    """ function takes a table as the input and apply boarder around the table
        in order to avoid error in the nextGen function
        function add new rows composed with 0s in the beggining and the end of the table
        and add 0 in the beggining and the end of each row """
    grid = [[0]*len(grid[0])]+grid+[[0]*len(grid[0])]
    current_grid = []
    for row in grid:
        row = [0] + row + [0]
        current_grid.append(row)
    return current_grid


def nextGen(current_grid):
    """function expects a two-dimensional table as the argument
        Given the current grid,
        function returns a new next grid by applying the rules of gmae of life"""
    current_grid = boardermaker(current_grid)
    new_grid = []
    for row in range(1,7):
        new_row = []
        for cell in range(1,8):
            neighbor_count = 0
            if current_grid[row-1][cell-1] == 1:
                neighbor_count += 1 
            if current_grid[row-1][cell] == 1:
                neighbor_count += 1
            if current_grid[row-1][cell+1] == 1 :
                neighbor_count += 1
            if current_grid[row][cell-1] == 1:
                neighbor_count += 1
            if current_grid[row][cell+1] == 1:
                neighbor_count += 1
            if current_grid[row+1][cell-1] == 1:
                neighbor_count += 1
            if current_grid[row+1][cell] == 1:
                neighbor_count += 1
            if current_grid[row+1][cell+1] == 1:
                neighbor_count += 1
                
            if current_grid[row][cell] == 1:
                if neighbor_count == 2:
                    new_row.append(1)
                elif neighbor_count == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
            else:
                if neighbor_count == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
        new_grid.append(new_row)
        
    return new_grid

  


# prog 6
def life():
    """ function reads data for the initial grid from a text file which is given the user's keyboard,
        function will then prints the numbers of generations of new grids, number is given by user's keyborad
        After printing program will ask the user if they would like to save the data,
        if use says Yes('Y') it will save the latest generation as a text file 
        function expects no arguments and does not return any value """
    current_grid = []
    while True:
        filename = input("Enter input file name: ")
        try:
            inFile = open(filename, "r")
            break
        except:
            print("No such file. Try again.")
    for line in inFile:   
        separated = line.split()
        current_grid.append(list(separated[0]))
    inFile.close() 
    while True:
        try:
            generation = int(input("How many new generations would you like to print "))
            break
        except:
            print("Not a valid number")
        
    for gen in range(0, generation+1):
        if gen == 0:
            new_grid0 = ""
            for row in current_grid:
                new_row0 = ""
                for cell in row:
                    if cell == "1":
                        new_row0 += "* "
                    else:
                        new_row0 += ". "
                new_grid0 += new_row0 + "\n"
            print("Generation: ", gen)
            print(new_grid0)
        else:
            current_grid = boardermaker(current_grid)
            new_grid1 = []
            new_grid2 = ""
            for row in range(1,7):
                new_row1 = []
                new_row2 = ""
                for cell in range(1,8):
                    neighbor_count = 0
                    if current_grid[row-1][cell-1] == "1":
                        neighbor_count += 1 
                    if current_grid[row-1][cell] == "1":
                        neighbor_count += 1
                    if current_grid[row-1][cell+1] == "1" :
                        neighbor_count += 1
                    if current_grid[row][cell-1] == "1":
                        neighbor_count += 1
                    if current_grid[row][cell+1] == "1":
                        neighbor_count += 1
                    if current_grid[row+1][cell-1] == "1":
                        neighbor_count += 1
                    if current_grid[row+1][cell] == "1":
                        neighbor_count += 1
                    if current_grid[row+1][cell+1] == "1":
                        neighbor_count += 1
                        
                    if current_grid[row][cell] == "1":
                        if neighbor_count == 2:
                            new_row1.append("1")
                            new_row2 +="* "
                        elif neighbor_count == 3:
                            new_row1.append("1")
                            new_row2 +="* "
                        else:
                            new_row1.append("0")
                            new_row2 +=". "
                    else:
                        if neighbor_count == 3:
                            new_row1.append("1")
                            new_row2 +="* "
                        else:
                            new_row1.append("0")
                            new_row2 +=". "
                new_grid1.append(new_row1)
                new_grid2 += new_row2 + "\n"

            current_grid = new_grid1
            print("Generation: ", gen)
            print(new_grid2)
    answer = input("Would you like to save the latest generation?('y' to save): ")
    if answer == 'y':
        while True:
            try:
                savefilename = input("Enter destination file name: ")
                outFile = open(savefilename, "x")
                for cell in current_grid:
                    writestring = ''.join(cell)
                    outFile.write(writestring+"\n")
                outFile.close()
                print("End of program.")
                break
            except:
                overwrite = input("Do you want to overwrite that file? ('y' to continue): ")
                if overwrite == "y":
                   outFile = open(filename, "w")
                   for cell in current_grid:
                        writestring = ''.join(cell)
                        outFile.write(writestring+"\n")
                   outFile.close()
                   print("End of program.")
                   break
                else:
                   continue

    else:
        print("End of program.")

        
