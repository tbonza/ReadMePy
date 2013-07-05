# write function for make.binary

def make_binary(matrix):
    # assign number or rows & columns to variables

    # clean up this nonsense
    r = num_row(matrix)
    c = num_col(matrix, 1)
    for i in range(r):
        print r
        for j in range(c):
    # with list comprehensions

            if(is_blank(matrix)== True):
                cell = 0
            elif(is_blank(matrix)== False):
                cell = 1
                
    return matrix

def is_blank(matrix):
    # is a cell blank?
    pass
    




