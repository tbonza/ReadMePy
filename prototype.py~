# Required libraries
import numpy as np

class prototype:
    '''
    prototype is the python2.7 equivalent for protoype.R
    found in the ReadMe library
    '''
    def RemoveNonvariant(tab):
        '''
        This function assumes that tab is an array. Still need
        to convert int to double when x.astype(double) isn't
        working
        '''
        ncols = len(tab[0]) # Assumes tab is an array
        i = 3
        while(i < ncols):
            i += 1
            m = np.mean(tab[:,i]) # convert int to double here??
            if(m == 1 or m == 0):
                # tab (below) slices out a column and compares
                # the remaining columns...otherwise we're good
                # make sure this function does that
                tab = tab[:\,-i]
                i -= 1
                ncols -= 1
        return tab

    def MakeBinary(tab):
        # find the shape of the array
        x = tab.shape
        # assign # of rows, columns as r & c
        r = x[0]
        c = x[1]
        for i in range(r):
            print r
        for j in range(c):
            if 
            
        
        
             

