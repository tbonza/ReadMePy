# write function for make.binary
import matrix_operations as mo

def make_binary(matrix):
    # assign number or rows & columns to variables
    if(is_blank(matrix) == True):
        cell = 0
    elif(is_blank(matrix) == False):
        cell = 1
                
    return matrix

def is_blank(matrix):
    '''
    This function assumes that when a file is read, empty cells
    will be assigned as 'None'. Given this assumption we can
    determine whether a cell, or list item, is empty.
    '''
    if check_cell(matrix) is None:
        return True
    elif check_cell(matrix) is not None:
        return False
    else:
        return "Error: cell is not designated as int or none"
  
  
def check_cell(matrix):
    # check each cell in matrix
    # clean up this nonsense
    # with list comprehensions
    for row in range(mo.num_row(matrix)):
        for cell in range(len(mo.get_row(matrix, row))):
            print  mo.get_row(matrix,row)[cell], "\t"
