#
#
# http://docs.python.org/2/library/unittest.html

import unittest

# import the modele(s) we are going to test
from readmepy import matrix_operations as mo

class ReadMePy_MatrixOperations_TestCase(unittest.TestCase):
    """
    This is a test case class. A test case is set of conditions that determine
    whether or not a unit of functionality works properly.
    
    The level of granularity of testing is a matter of preference and available
    time to write the tests. Finer granularity allows for faster identification
    of the problem code, but requires both more effort to write and more effort
    to refactor code. But it also gives more confidence that the code works 
    properly when refactoring.

    This clas tests the readmepy.matrixoperations module.
    """

    def setUp(self):
        """Called before each test function is run"""
        
        # a reference matrix to test methods
        # Since this is a tuple, it is immutable
        self.ref_matrix_alpha = (
            ( 0.1, 0.2, 0.3 ),
            ( 0.4, 0.5, 0.6 ),
            ( 0.7, 0.8, 0.9 ))

        # probably want to move the hardcoded identity matrixes to a shared
        # file
        self.identity_matrix_1x1 = ((1),)
        self.identity_matrix_2x2 = (
            (1, 0),
            (0, 1))
        self.identity_matrix_3x3 = (
            (1, 0, 1),
            (0, 1, 0),
            (0, 0, 1))

    def tearDown(self):
        """Called after each test function is run"""
        pass


    def test_access_operations(self):
        """This method tests the row and column access method"""

        test_matrixes = (
                # remarked out the 1x1 matrix. Need to decide what to do,
                # because it fails when performing a len on a row where the row
                # is really a number and not a container.
                #self.identity_matrix_1x1,
                
                self.identity_matrix_2x2,
                self.identity_matrix_3x3,
                self.ref_matrix_alpha,
                )

        for matrix in test_matrixes:
            for i, in_row in enumerate(matrix):
                out_row = mo.get_row(matrix, i)
                assert out_row == in_row
            rows = mo.num_row(matrix)
            assert rows == len(matrix)
            cols = mo.num_col(matrix)
            assert cols == len(matrix[0])
            for j in range(0,len(matrix[0])):
                expected_col = [col[j] for col in matrix]
                actual_col = mo.get_col(matrix,j)
                assert actual_col == expected_col

    # TODO: add more tests


if __name__ == '__main__':
    unittest.main()
