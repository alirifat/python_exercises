# corpus: large body of text

# in order to apply methods to a text, first identify it as a text in NLTK library
text = nltk.Text('file.txt')
text.concordance('surprize')

# basic statistics on text
# 1. average word length
# 2. average sentence length
# 3. the number of times each vocabulary appears in text - lexical diversity

# raw() function gives the content of the text without any linguistic processing
# sents() gives the number of sentences in the text

# corpuses in nltk library
# 1. gutenberg e-books
from nltk.corpus import gutenberg
for fileid in gutenberg.fileids():
    ...
# 2.web & chat text
from nltk.corpus import webtext
for fileid in webtext.fileids():
    ...
# 3. Brown corpus
from nltk.corpus import brown
