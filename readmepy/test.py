# write function for make.binary
import matrix_operations

def make_binary(matrix):
    # assign number or rows & columns to variables
    if(check_cell(is_blank(matrix)) == True):
        cell = 0
    elif(check_cell(is_blank(matrix)) == False):
        cell = 1
                
    return matrix

def is_blank(matrix):
    '''
    This function assumes that when a file is read, empty cells
    will be assigned as 'None'. Given this assumption we can
    determine whether a cell, or list item, is empty.
    '''
    if cell is None:
        return True
    elif cell is not None:
        return False
    else:
        return "Error: cell is not designated as int or none"
    
def check_cell(matrix):
    # check each cell in matrix
    '''
     r = num_row(matrix)
    c = num_col(matrix, 1)
    for i in range(r):
        print r
        for j in range(c):
    '''
    # clean up this nonsense
    # with list comprehensions
    for cell in range(num_row(matrix)):
        get_col(matrix, cell)




