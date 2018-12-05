import spacy
import en_core_web_sm
nlp = en_core_web_sm.load()

def textInAList(text):
    '''Puts text into a list and removes beginning whitespace.'''
    listOfSentences = text.split(".")[:-1]
    result = []
    for sentence in listOfSentences:
        newsentence = sentence.strip(" ")  # removes whitespace before sentence
        result.append(newsentence)
    return result


def nominalizationIdentification(inputText):
    '''
    Puts [Nominalization] next to sentences that have a nominalization
    as their subject.
    '''
    listOfSuffixes = ['ness', 'sis', 'tion', 'sion', 'cion']
    textInAlist = textInAList(inputText)
    outputSentence = []
    finalOutputSentence = ""
    for sentence in textInAlist:
        nlpSentence = nlp(sentence)
        for i,word in enumerate(nlpSentence):
            if word.dep_ == 'nsubj' or word.dep_ == 'nsubjpass':
                subject = word.text
                if subject[-4:] in listOfSuffixes or subject[-3:] in listOfSuffixes:
                    outputSentence.append(word.text + "[Nominalization]")
                else:
                    outputSentence.append(word.text)
            # puts a period on the last word of the sentence
            elif i == len(nlpSentence)-1:
              outputSentence.append(word.text + ".")
            else:
                outputSentence.append(word.text)

    outputAsString = " ".join(outputSentence)
    finalOutputSentence += outputAsString
    return finalOutputSentence

