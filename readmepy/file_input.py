# Inputs text used in ReadMePy
# for Clinton Demo

path = '/home/ty/summer_project/clintonposts/'

document = path + 'control.txt'

def read_local(document): 
    '''
    Reads in a local file 
    '''
    f = open(document, 'r')
    return f


def assign_list(document):
    '''
    file becomes a list
    '''
    assign_list = []
    for line in read_local(document).readlines():
        assign_list.append(line)
    return assign_list

def strip_split(document):
    '''
    Strips '\n' and separates each list
    item by ','
    '''
    cleaned_list = []
    for line in range(len(assign_list(document))):
        l = assign_list(document)[line].strip().split(',')
        cleaned_list.append(l)
    return cleaned_list


def tuple_list(document):
    '''
    list becomes tuple list
    '''
    okey = strip_split(document)
    pokey = [(okey[line][0],okey[line][1],okey[line][2])
            for line in
            range(len(strip_split(document)))]
    return pokey


# Quick test
#for i in range(len(tuple_list(document)[0:5])):
#    print tuple_list(document)[i]
