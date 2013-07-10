# This is the main file. Functions share the same name as 
# their R counterparts in ReadMe

import matrix_operations
import binary_operations

def remove_nonvariant(matrix):
        '''
        Removes extreme columns then 
        normalizes the matrix to values between 1 
        and 0. It's named this way to match the
        function in the R library ReadMe. 
        '''
        return matrix_operations.normalized_matrix(matrix_operations.remove_extreme_cols(matrix))

def make_binary(matrix):
        '''
        Changes blank cells to 0 and populated cells
        to 1
        '''
        return binary_operations.assign_binary(matrix)


        
        
             

