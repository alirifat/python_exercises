from nltk.book import *
print(text1)

# .concordance() method in nltk gives occurance of a given word with some context
# in the text

# .similar() method gives the words that are used in similar range of context of
# a given word

# .common_contexts() gives the contexts that are shared by two or
# more words in the given text. ex. text.common_contexts(['word1', 'word2'])

# .dispersion_plot() determines the location of a given word in a text and returns
# a plot which shows the locations in the text

# token: the technical name for a sequence of characters that treated as a group
print(len(text3)) # gives the total number of occurances of words in the text
# including double or more counting
print(len(set(text3))) # gives the number of unique words in the text
# it is important to lowercase tokens before extracting unique ones.
# also it is possible to eliminate numbers so that the unique words consist
# only from alphabetical characters.

# the average number of occurance of a word - also called 'lexical_diversity'
print(len(text3)/len(set(text3)))

# .count() gives the total number of occurances of a given word
print(text3.count('smote')) # gives how many times 'smote' is occured in the text
# how many percentage of the text consists of the given word
print((text3.count('smote') / len(text3)) * 100)

# frequecny distribution of a text gives us how many percent of the text consists
# of the given word?
# FreqDist() takes an iterable of tokens as input and returns the fequency distr.
# It is a good practice to examine frequency distribution of a text since the most
# frequent tokens may not be the most informative ones.
# On the other hand, `hapaxes` refers to the words that only occur once in the text
# Those, hapaxes, may not be informative, as well.

# `collacation` is a sequence of words that are often used together ex. red wine
# in order to identify collacations use `n-gram`
# `bigram` is a two-word sequence of words

# Another approach is to look how the length of words are distributed. i.e. how
# many percents of the text consists of three character words.

 # `word sense disambiguation` which sense of a given word was intended in the
 # given context. Since, words may have different meanings by the context, it is
 # important to know this concept. A human can easily detect the intended meaning
 # but it is not the case for a computer.
 
