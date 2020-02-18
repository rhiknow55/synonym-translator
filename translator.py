# Be able to read a text file and replace all non=stopwords with synonyms
print("tranloator")

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords # Words such as "a", "the"
from nltk.corpus import wordnet
import random

filename = "test.txt"

# TODO: open file first like this and read or just directly read?
# with open(filename) as fin:
# file_content = open(filename).read()

# print(tokens)
stop_words = stopwords.words("english")
punctuations = ['A', ',', ';', '.', "'"]

def translate(input):
    tokens = []
    tokens = word_tokenize(input)

    validwords = [word for word in tokens if not word in stop_words and not word in punctuations]

    synonymsDict = getSynonyms(validwords)

    res = createReplacedOutput(tokens, synonymsDict)

    print(res)
    return res


# for syn in wordnet.synsets()

def getSynonyms(validwords):
    # Dict of word to array of synonyms
    pairs = {}

    # Create the dictionary of synonym key value pairs
    for word in validwords:
        if word in pairs.keys():
            continue
        else:
            pairs[word] = []

        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                name = l.name()
                if name != word and name not in pairs[word]:
                    pairs[word].append(name)

    return pairs

def createReplacedOutput(tokens, pairs):
    res = ""

    # Now just replace the original string with these replacements
    for i in range(len(tokens)):
        word = tokens[i]
        word_to_print = ""
        if word in pairs.keys() and pairs[word]:
            index = random.randint(0, len(pairs[word]) - 1)
            word_to_print = pairs[word][index]
        else:
            word_to_print = word

        # TODO: only space if not punctuation
        endstring = " "
        if i != len(tokens) - 1:
            # Check if any punctuation
            for punct in punctuations:
                if punct in tokens[i+1]:
                    endstring = ""

        res += (word_to_print + endstring)
        # print(word_to_print, end=endstring)

    return res

translate("hello test this one find hate like")
