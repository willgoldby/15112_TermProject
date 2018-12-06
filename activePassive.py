import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()

def textInAList(text):
    '''Puts text into a list and removes beginning whitespace.'''
    listOfSentences = text.split(".")[:-1]
    result = []
    for sentence in listOfSentences:
        newsentence = sentence.strip(" ") # removes whitespace before sentence
        result.append(newsentence)
    return result

def getSentenceParts(text):
    '''Returns a dictionary of words and their function within a sentnece.'''
    sentenceParts = dict()
    tokenizedSentence = nlp(text)
    for i,word in enumerate(tokenizedSentence):
        sentenceParts[word.dep_] = word.text
        wordDepString = str(word.dep_) + "Pos"
        sentenceParts[wordDepString] = i
    if 'auxpass' in sentenceParts:
        sentenceParts['passive'] = True
    else:
        sentenceParts['passive'] = False

    if sentenceParts['passive'] == True: # For debugging purposes
        print (sentenceParts)
    return sentenceParts


def chagnePassiveToActive(dictOfSentenceParts, sentence):
    '''Changes a passive sentence to active. If sentence is active, returnsi it.'''
    # beforeAgent = [] # fixes 'referenced before assignment' problem
    sentenceInList = sentence.split(" ")

    # Checks if sentence has an agent position in order to avoid sentences that
    # have passive constructions but no agent, i.e., 'to be used daily in an
    # office environment'.
    if dictOfSentenceParts.get('agentPos') and dictOfSentenceParts['passive'] == True :
        try:
            beforeAgent = dictOfSentenceParts['agentPos'] - 1
        except:
            pass
        # For sentence that are of the form "Jill was lied TO by Sam."
        if sentenceInList[beforeAgent] == 'to':
            activeSentence = f"{dictOfSentenceParts['pobj']} {dictOfSentenceParts['ROOT']} to {dictOfSentenceParts['nsubjpass']}"
            return activeSentence

        try:
            beforePassiveSubject = dictOfSentenceParts['nsubjpassPos'] - 1
        except:
            pass
        # For sentence with a non-personal noun, i.e., "The ball was kicked by Sam."
        if sentenceInList[beforePassiveSubject] in ("The", "a", "an", "A", "An", "the"):
            activeSentence = f"{dictOfSentenceParts['pobj']} {dictOfSentenceParts['ROOT']} {sentenceInList[beforePassiveSubject]} {dictOfSentenceParts['nsubjpass']}"
            return activeSentence

        else:
            # For regular passive like "Jim was kicked by Sam."
            activeSentence = f"{dictOfSentenceParts['pobj']} {dictOfSentenceParts['ROOT']} {dictOfSentenceParts['nsubjpass']}"
            return activeSentence
    return sentence

def outputText(text):
    '''Takes a text and returns it with the passive sentences changed to active sentences.'''
    sentencesInAList = textInAList(text)
    result = []
    for sentence in sentencesInAList:
        sentenceParts = getSentenceParts(sentence)
        sentenceToAppend = chagnePassiveToActive(sentenceParts, sentence)
        result.append(sentenceToAppend)
        finalOutput = ".".join(result)
        finalOutput += "."
    return finalOutput


