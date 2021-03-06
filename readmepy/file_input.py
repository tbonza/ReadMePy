# Inputs text used in ReadMePy
# for Clinton Demo

# Create file path
def document(path, filename):
    '''
    Concatenate the file path 
    and file name. 
    '''
    return path + filename

# Define parameters for document
path = '/home/ty/summer_project/clintonposts/'
document = document(path, 'control.txt')

# File input functions
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


def word_list(document):
    '''
    All words to a list 
    for unigrams, bigrams, trigrams.
    '''
    okey = strip_split(document)
    return okey


# Quick test
#for i in range(len(tuple_list(document)[0:5])):
#    print tuple_list(document)[i]

# Longer test
#for i in range(len(tuple_list(document))):
#    print tuple_list(document)[i]

# Some numbers
#print len(tuple_list(document))


