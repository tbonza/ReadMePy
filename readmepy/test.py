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
    determine whether a cell, or list item, is empty. If a cell
    is empty, assigned as 'None', then the cell will be returned
    as False. Otherwise, the cell is returned as True.
    '''
    bool_blank = [[cell == None for cell in row] for row in matrix]
    return bool_blank
