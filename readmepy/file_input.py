# Inputs text used in ReadMePy
# This file is being tested and not linked to any other functions

import nltk # Used to clean up html
import requests 

path = '/home/ty/summer_project/clintonposts/'

def input_multiple_f(path, control): #needs work
    '''
    Takes a control file with a list of file
    names, cocatenates the name with a file
    path, then returns the location of each
    document in the control file.
    '''
    file_list = []
    for file_name in read_local(control):
        file_list.append(path+file_name)
    return file_list

def read_local(document): #works
    '''
    Reads local files into
    ReadMePy
    '''
    f = open(document).read()
    return f

def read_html(url): # This needs work
    '''
    Reads html files into ReadMePy
    '''
    r = requests.get(url)
    text = r.text()
    return text

def parse_control_f(control):
    '''
    Parses control file,
    specific to clintonposts
    example used in ReadMe
    '''
    pass
