import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()

# Returns a text object
def readText(path):
    with open(path, 'r') as f:
        return f.read()

# Creates a text file
def returnListInText(nameToSave, content):
    with open(nameToSave, "w") as f:
        f.write(content)

# Gets the distance between subject and verb
def getDistanceBetweenWords(sentence, subject, verb):
    textAsList = sentence.split(" ")
    wordsBetween = textAsList[textAsList.index(subject) + 1: textAsList.index(verb)]
    result = len(wordsBetween)
    return result

# Puts sentences into a list
def putTextInList(text):
    return text.split(".")[:-1]

# Gets the length of a sentence
def getLengthOfSentence(text):
    textAsList = text.split(" ")
    length = len(textAsList)
    return length


# Returns a dictionary with the sentence number, the subject, verb, passive verb,
# sentence length, and position of verb.
def getSentenceData(text):
    allSentenceData = [] # List that will store dictionary data for each sentence.
    textInList = putTextInList(text) # Puts text into a list. Each sentence is an element.
    count = -1
    for sentence in textInList:
        count += 1
        tokenSentence = nlp(sentence) # Tokenizes each sentence.
        dictofData = dict() # Dictionary to store sentence values.
        for word in tokenSentence: # Get subject, ver and passive verb and puts into the dictionary.
            if word.dep_ == 'nsubj':
                dictofData['nsubj'] = word.text
                dictofData["sentence"] = count
            if word.dep_ == "auxpass":
                dictofData["passive"] = word.text
            if word.dep_ == "ROOT":
                dictofData["ROOT"] = word.text
        allSentenceData.append(dictofData)
        dictValues = allSentenceData[count] # Gets dictionary so subject and verb can be passed into distanceBetweenSubjectVerb
        distanceBetweenSubjectVerb = getDistanceBetweenWords(sentence, dictValues['nsubj'], dictValues['ROOT'])
        lenghtOfSentence = getLengthOfSentence(sentence)
        dictofData["verbDistance"] = distanceBetweenSubjectVerb
        dictofData["sentLength"] = lenghtOfSentence
    return allSentenceData


someRandomText = "Artificial intelligence has captured the popular imagination since Mary Shelley’s Frankenstein. Hollywood has trafficked in sci-fi fantasies for the last two decades, portraying scenarios where humans and machines coexist, either as equals or enemies. It has given us The Terminator, Blade Runner, and Ex Machina. "



