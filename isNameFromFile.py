# Takes in a list of names from a file and returns what percent of the names are recognized
import re
import unidecode
import nltk
import numpy

fileName = input("Please enter the name of the text file you want to evaluate: ")

# just reading it
# deletes diacritics
nameList = []
with open(fileName, 'rt', encoding='utf-8') as fn:
    for line in fn:
        line = unidecode.unidecode(line)
        nameList.append(line.strip())

print(nameList)

# make names in the format First Last (vs FiRst, etc)
def makeTitle(aList):
    newList = []
    for i in aList:
        newList.append(i.title())
    return newList


# remove punctuation within names
def noApostrophes(aList):
    newList = []
    for i in aList:
        newList.append(re.sub("\'", "", i))
    return newList


def recognize(aList):
    names = []
    for i in aList:
        tokens = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(tokens)
        for entity in nltk.chunk.ne_chunk(tagged):
            if type(entity) == nltk.tree.Tree:
                if entity.label() == 'PERSON':
                    names.append(i)
                    break
    print(names)
    print("The percent accuracy on this list was " + str(100 * (len(names)/len(aList))))

allTitle = makeTitle(nameList)
noApostrophesList = noApostrophes(nameList)
both = makeTitle(noApostrophesList)

recognize(nameList)
recognize(allTitle)
recognize(noApostrophesList)
recognize(both)




# more ideas:
# delete part of name before apostrophe in first name
# (e.g. De'Aaron -> Aaron, D'Angelo -> Angelo)



