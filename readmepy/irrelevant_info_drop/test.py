# Test functions for irrelevent_info_drop

# Function for non-english language text
'''
Sources:
  http://www.velvetcache.org/2010/03/01/looking-up-words-in-a-dictionary-using-python

'''
from nltk.corpus import wordnet

def get_test_phrase(document):
    '''
    This function grabs the first sentence of the document
    in question to test if it is in english or not.
    '''
    pass
   # return words

words = ["cookies","vous","hipsters","chocolate","monty"]

def is_english(words):
    '''
    Returns a list of booleans where a word is True
    if it is english; False if it is not english.
    Errors append 'None' to the list
    '''
    for word in words:
        english = []
        synsets = wordnet.synsets(word)
        if word in synsets:
            english.append(True)
        elif word not in synsets:
            english.append(False)
        else:
            english.append(None)
    return english

# caution: random scripting below this line
synsets = wordnet.synsets('cookies')
print synsets
