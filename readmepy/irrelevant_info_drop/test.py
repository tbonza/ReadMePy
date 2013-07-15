# Test functions for irrelevent_info_drop

# Function for non-english language text
'''
Sources:
  http://www.velvetcache.org/2010/03/01/looking-up-words-in-a-dictionary-using-python

'''
from nltk.corpus import wordnet

words = ["cookies","vous","hipsters","chocolate","monty"]


for word in words:
    synsets = wordnet.synsets(word)
    print synsets

synsets = wordnet.synsets('cookies')
print synsets
