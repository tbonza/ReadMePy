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
             
'''
def tuple_list(document):
    
    Read each line in as a tuple
    
    tuple_list = []
    lines = read_local(document)
    for line in lines.readlines():
        temp = line
        length = len(temp) - 1
        tuple_list.append(temp[0] = temp[1:length]
    return tuple_list

'''
