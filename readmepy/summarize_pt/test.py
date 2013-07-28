# Test functions for summarize_pt

# Generating unigrams, bigrams and trigrams
import file_input
from sklearn.feature_extraction.text import CountVectorizer

# working from the tutorial
vectorizer = CountVectorizer(min_df=1)

corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?']

# tokenize and count the word occurrences of a minimalistic 
# corpus of text documents
X = vectorizer.fit_transform(corpus)

# The default configuration tokenizes the string by extracting
# words of at least 2 letters. The specific function that does 
# this step can be requested explicitly:
