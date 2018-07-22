#Sudoku
def check_sudoku(grid):
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] < 1 :
                return False
            # check value is within 1 through n.
            # for example a 2x2 grid should not have the value 8 in it
            elif grid[row][col] > 9:
                return False
    # check the sub-matrix
    for i in  range (0,8,3):
        for j in range (0,8,3):
            x = grid [i:i+3,j:j+3]
            y = x.reshape((1,9))
            print(x)
            for row in y:
                if sorted(list(set(row))) != sorted(row):
                    return False
    # check the rows
    for row in grid:
        if sorted(list(set(row))) != sorted(row):
            return False
    # check the cols
    cols = []
    for col in range(len(grid)):
        for row in grid:
            cols += [row[col]]
        # set will get unique values, its converted to list so you can compare
        # it's sorted so the comparison is done correctly.
        if sorted(list(set(cols))) != sorted(cols):
            return False
        cols = []

    # if you get past all the false checks return True
    return True
import numpy as np
z = np.random.randint(1,9, size=(9, 9))
a = np.array ([[8,2,9,5,2,1,7,3,6],
              [2,5,7,8,6,3,9,1,4],
              [1,6,3,7,4,9,2,5,8],
              [3,2,5,1,9,6,4,8,7],
              [4,9,8,3,5,7,6,2,1],
              [7,1,6,4,8,2,3,9,5],
              [9,8,4,2,7,5,1,6,3],
              [6,7,1,9,3,8,5,4,2],
              [5,3,2,6,1,4,8,7,9]])
print (a)
check_sudoku(a)
