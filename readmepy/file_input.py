# Inputs text used in ReadMePy
# for Clinton Demo
#
# This file is being tested and not linked to any other functions

path = '/home/ty/summer_project/clintonposts/'

document = path + 'control.txt'

def read_local(document): 
    '''
    Reads local files into
    ReadMePy by each line
    '''
    f = open(document, 'r'
    return f

def assign_tuple(document):
    '''
    line becomes a tuple
    '''
    tuple_list = []
    for line in read_local(document).readlines():
        t = line
        tuple_list.append(t)
    return tuple_list
             
# Test list to tuple for control.txt

test = 'This.is, the first, line of the file.\n'

test2 = 'That.is, the second, line of the file.\n'

okey = [test.strip().split(','), test2.strip().split(',')]

pokey = [(okey[line][0],okey[line][1],okey[line][2]) for line in range(len(okey))]
