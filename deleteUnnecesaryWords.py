wordsThatCanBeDeleted = ['really', 'very', 'totally', 'completely', 'absolutely', 'literally']

def removeUnnessaryWords(sentence):
    '''Removes words from a sentence that are in the list wordsThatCanBeDeleted'''
    revisedSentence = []
    sentenceAsList = sentence.split(" ")
    for word in sentenceAsList:
        if word not in wordsThatCanBeDeleted:
            revisedSentence.append(word)

    revisedSentence = (" ").join(revisedSentence)
    return revisedSentence







