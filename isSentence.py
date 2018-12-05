import spacy
import itertools
import en_core_web_sm
nlp = en_core_web_sm.load()


def isSentence(changedSentence, originalSentence):
    '''
    Takes a changed sentence and the original sentence and returns True if
    they are close enough in meaning. If not, function return False.
    '''
    # Initializes the variables needed.
    originalSubject = None
    originalSentenceVerb = None
    changedSubject = None
    changedSentenceVerb = None

    # Makes both sentences Doc objects.
    nlpChangedSentence = nlp(changedSentence)
    nlpOriginalSentence = nlp(originalSentence)

    # Initializes dictionaries that will hold parts of speech data.
    sentenceElementsChangedSentence = dict()
    sentenceElementsOriginalSentence = dict()

    # Loops over both lists using itertools and populate dictionaries with part of speech data.
    for changedWord, originalWord in itertools.zip_longest(nlpChangedSentence, nlpOriginalSentence):

        # Once one of the lists ends, itertools makes the other list populate with None.
        # This makes sure None doesn't get added to dictionaries.
        if changedWord == None:
            continue
        sentenceElementsChangedSentence[changedWord] = (changedWord.dep_, changedWord.pos_)

        if originalWord == None:
            continue
        sentenceElementsOriginalSentence[originalWord] = (originalWord.dep_, originalWord.pos_)

    # Loops over both dictionaries and checks for conditions
    for key1, key2 in itertools.zip_longest(sentenceElementsChangedSentence, sentenceElementsOriginalSentence):
        similarity = nlpOriginalSentence.similarity(nlpChangedSentence)
        if key1 == None:
            continue
        if key2 == None:
            continue

        # Gets the subject and verb from the changed sentence and the original sentence.
        if sentenceElementsChangedSentence[key1][0] == 'ROOT' and sentenceElementsChangedSentence[key1][1] == 'VERB':
            changedSentenceVerb = key1
        if sentenceElementsOriginalSentence[key2][0] == 'ROOT' and sentenceElementsOriginalSentence[key2][1] == 'VERB':
            originalSentenceVerb = key2

        if (sentenceElementsChangedSentence[key1][0] == 'nsubj' or sentenceElementsChangedSentence[key1][0] == 'nsubjpass') and ((sentenceElementsChangedSentence[key1][1] == 'NOUN') or (sentenceElementsChangedSentence[key1][1] == 'PRON')):
            changedSubject = key1

        if (sentenceElementsOriginalSentence[key2][0] == 'nsubj' or sentenceElementsOriginalSentence[key2][0] == 'nsubjpass') and ((sentenceElementsOriginalSentence[key2][1] == 'NOUN') or (sentenceElementsOriginalSentence[key2][1] == 'PRON')):
            originalSubject = key2


    # Replaces elements in dictinary with None when they are empty.
    if changedSentenceVerb == None:
        changedSentenceVerb = nlp("None")
    if changedSubject == None:
        changedSubject = nlp("None")

    # Test to see if the two sentences are similar enough. If so, returns True.
    try:
        if (changedSentenceVerb.text == originalSentenceVerb.text) and \
                (originalSubject.text == changedSubject.text) \
                and (similarity > .91):
            return True
    except:
        return False





