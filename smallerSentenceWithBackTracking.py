from isSentence import *
from isComplete import *
import spacy
import en_core_web_lg
nlp = en_core_web_lg.load()

def makeSentenceSmaller(blockOfText):
    result = []
    blockOfTextAsList = blockOfText.split(".")
    for elem in blockOfTextAsList: # Removes white space
        if (elem == "") or (elem == " "):
            blockOfTextAsList.remove(elem)
    for i, sentence in enumerate(blockOfTextAsList):
        revisedSentence = backtrackingWithSentence(sentence)
        result.append(revisedSentence)
    result = ".".join(result)
    result = result + "."
    return result


def backtrackingWithSentence(sentence):
    # Not sure what the base case is here?
    if isComplete(sentence):
        return sentence

    # Put sentence into a list so individual words can be removed.
    sentenceInList = sentence.split(" ")

    for i, word in enumerate(sentenceInList):

        if word == '': # Removes white space
            sentenceInList.remove(word)

        # Remove a word from the sentence
        sentenceWithWordRemoved = sentenceInList[:i] + sentenceInList[i+1:]

        # Put the sentence back into a string
        sentenceWithWordRemovedAsString = " ".join(sentenceWithWordRemoved)

        # print("Original sentence:", sentenceInList)
        # print("Sentence with word removed:", sentenceWithWordRemovedAsString)

        # Check if sentence is a valid sentence
        if isSentence(sentenceWithWordRemovedAsString, sentence):
            sentence = sentenceWithWordRemovedAsString

            # Recusive call
            tmpSolution = backtrackingWithSentence(sentence)
            if tmpSolution != None:
                return tmpSolution

        # Insert word that was removed back into sentence
        sentenceWithWordRemoved.insert(i, word)

    return sentence





