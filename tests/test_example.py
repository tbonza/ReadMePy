#
#
# http://docs.python.org/2/library/unittest.html

import unittest

# import the modele(s) we are going to test
#from readmepy import x

class ReadMePy_Example_TestCase(unittest.TestCase):
    """
    This is a test case class. A test case is set of conditions that determine
    whether or not a unit of functionality works properly.
    
    The level of granularity of testing is a matter of preference and available
    time to write the tests. Finer granularity allows for faster identification
    of the problem code, but requires both more effort to write and more effort
    to refactor code. But it also gives more confidence that the code works 
    properly when refactoring.

    This clas demonstrates how to write a simple unittest based test case.
    """

    def setUp(self):
        """Called before each test function is run"""
        pass


    def tearDown(self):
        """Called after each test function is run"""
        pass

    def test_Fails(self):
        """Example test for the test case"""
        # assert statement. The value of the expression after the assert
        # statement determines if this test function passes or fails.
        # if the expression evalues to None or False (if not expression)
        # then an AssertionError is raised
        # otherwise, the code passes through. If the test method does not
        # raise an exception, it is considered a passing tests
        # you can have multiple asserts in a test method. The first one that
        # evaluates to a not expression (None or False)
        # if a method is provided as the expression and it raises an exception,
        # then that exception is raised instead of the AssertionError of this
        # test method
        assert False

    def test_Passes(self):
        assert 'Happy, happy, joy, joy!'
        assert True



if __name__ == '__main__':
    unittest.main()
