# write function for make.binary
import matrix_operations as mo


def is_blank(matrix):
    '''
    Assumes that when a file is read, empty cells will be assigned
    as 'None'. Given this assumption we can determine whether a 
    cell, or list item, is empty. If a cell is empty, assigned as 
    'None', then the cell will be returned as False. Otherwise, 
    the cell is returned as True.
    '''
    bool_blank = [[cell == None for cell in row] for row in matrix]
    return bool_blank


def assign_binary(matrix):
    '''
    Takes the boolean values assigned to the matrix by is_blank() 
    and converts them to 0 if the cell is designated as None
    when data was read into the program. 
    '''
    binary = 
    [[0 if cell == True else 1
      for cell in row]
     for row in t.is_blank(matrix)]
    return binary

        

        

