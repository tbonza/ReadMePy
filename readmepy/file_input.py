# Inputs text used in ReadMePy
# This file is being tested and not linked to any other functions

# Inputs text used in ReadMePy
# for Clinton Demo
#
# This file is being tested and not linked to any other functions

path = '/home/ty/summer_project/clintonposts/'

def read_local(document): 
    '''
Reads local files into
ReadMePy
'''
    f = open(document, 'r')
    return f

def tuple_list(document):
    '''
    Read each line in as a tuple
    '''
    tuple_list = []
    lines = read_local(document)
    for line in lines.readlines():
        temp = line
        
        tuple_list.append(
        temp[0] = temp[1:(len(temp)-1))
        )
    return tuple_list
