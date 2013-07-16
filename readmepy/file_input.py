# Inputs text used in ReadMePy
# This file is being tested and not linked to any other functions

path = ''

def input_multiple_f(path, control):
    '''
    Takes a control file with a list of file
    names, cocatenates the name with a file
    path, then returns the location of each
    document in the control file.
    '''
    for text_doc in control:
        document = path+text_doc
    return document

def read_local(document):
    '''
    Reads local files into
    ReadMePy
    '''
    f = open(document).read()
    return f

def parse_control_f(control):
    '''
    Parses control file,
    specific to clintonposts
    example used in ReadMe
    '''
    pass
