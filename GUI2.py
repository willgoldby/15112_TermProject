from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from productionCode import *
from activePassive import *
from deleteUnnecesaryWords import *
from nominalization import *
from smallerSentenceWithBackTracking import *
import re
from regexFixing import *

########################
#
#
# Create window for content and buttons
#
#
########################

# main window
root = Tk()

# A window pane for all content
paneForAllContent = ttk.Panedwindow(root, orient=HORIZONTAL)

# Put the window pane into root
paneForAllContent.pack(fill=BOTH, expand=True)


# A frame for buttons that will go inside paneForAllContent
frameForButtons = ttk.Frame(paneForAllContent, width=100, height=100, relief=SUNKEN)

# A frame for the text to go into paneForAllContent
frameForText = ttk.Frame(paneForAllContent, width=500, height=500)

# Put the frames inside the paneForAllContent
paneForAllContent.add(frameForButtons, weight=1)
paneForAllContent.add(frameForText, weight=4)


##############################
#
#
# Create buttons
#
#
##############################


#############################
# Button for loading text
#############################

# A button that will put text onto screen
loadTextButton = ttk.Button(frameForButtons, text = "Load your text")

# Button functionality
loadTextButton.config(command = lambda : getFilePathReadText())

# Puts button onto frameForButtons
loadTextButton.pack(anchor=W, padx=10, pady = 10)


####################################################
# Button for changing passive voice to active voice
####################################################

# Button for changing passive voice to active voice
changePassiveToActive = ttk.Button(frameForButtons, text="Change passive voice to active voice")

# Button functionality
changePassiveToActive.config(command= lambda : changePassiveSentencesToActive())

# Puts button onto frameForButtons
changePassiveToActive.pack(anchor=W, padx=10, pady=10)


###############################
# Button for nominalizations
###############################

# Button for nominalizations
checkForNominalizations = ttk.Button(frameForButtons, text="Check for nominalizations")

# Button functionality
checkForNominalizations.config(command= lambda : checkNominalizations())

# Puts button onto frameForButtons
checkForNominalizations.pack(anchor=W, padx=10, pady=10)


#########################################
# Button for removing unnecessary words
#########################################

# Button to remove unnecessary words
removeUncessaryWords = ttk.Button(frameForButtons, text = "Remove unnecessary words")

# Button functionality
removeUncessaryWords.config(command= lambda : removeUnnecessaryWordsFromText())


# Puts button onto frameForButtons
removeUncessaryWords.pack(anchor=W, padx=10, pady=10)


###################################
# Button for shortening sentences
###################################


# Button to remove unnecessary words
shortenSentences = ttk.Button(frameForButtons, text = "Shorten sentences")

# Button functionality
shortenSentences.config(command= lambda : shortenSentences() )


# Puts button onto frameForButtons
shortenSentences.pack(anchor=W, padx=10, pady=10)

################################
# Button for testing functions
################################

# Create button
# testButton = ttk.Button(frameForButtons, text="TEST BUTTON")

# Functionality
# testButton.config(command= lambda : insertEditedText())

# Place button onto frameForButtons

# testButton.pack(anchor=W, padx=10, pady=10)


###################################
#
# Functions for buttons
#
###################################

       ####################################################
#######   BUTTON FUNCTION  TO LOAD TEXT ONTO THE SCREEN    ##############
       ####################################################

# someText is a text frame object. Text
someText = Text(frameForText)

def getFilePathReadText():
    filename = filedialog.askopenfile('r')
    someText.insert(END, filename.read())
    someText.config(wrap='word')
    someText.pack()
    return filename

       ####################################################
#######   BUTTON FUNCTION  TO GET TEXT FROM TEXT BOX       ##############
       ####################################################

# Used for all functions because all functions need to get the text from
# the text box.

def getContentFromTextBox():
    content = someText.get("1.0", END)  # gets content in text frame
    return content

       ###############################################
#######   BUTTON FUNCTION  FOR ACTIVE TO PASSIVE      ##############
       ###############################################

def changePassiveSentencesToActive():
    onScreenText = getContentFromTextBox()
    changedText = outputText(onScreenText)
    inputText = fixErrors(changedText)
    someText.delete("1.0", END)
    someText.insert("1.0", inputText)


       ########################################################
#######   BUTTON FUNCTION  FOR REMOVING UNNECESSARY WORDS      ##############
       ########################################################

def removeUnnecessaryWordsFromText():
    onScreenText = getContentFromTextBox()
    changedText = removeUnnessaryWords(onScreenText)
    inputText = fixErrors(changedText)
    someText.delete("1.0", END)
    someText.insert("1.0", inputText)


       ########################################################
#######   BUTTON FUNCTION FOR CHECKING FOR NOMINALIZATIONS     ##############
       ########################################################

def checkNominalizations():
    onScreenText = getContentFromTextBox()
    changedText = nominalizationIdentification(onScreenText)
    inputText = fixErrors(changedText)
    someText.delete("1.0", END)
    someText.insert("1.0", inputText)


       ###############################################
#######   BUTTON FUNCTION  FOR SHORTENING SENTENCES   ##############
       ###############################################

def shortenSentences():
    onScreenText = getContentFromTextBox()
    changedText = makeSentenceSmaller(onScreenText)
    inputText = fixErrors(changedText)
    someText.delete("1.0", END)
    someText.insert("1.0", inputText)


################################
# Testing button functionality #
################################

def printFileContnet():
    stuffInTextFrame = someText.get("1.0", END)
    # print(stuffInTextFrame)

def sentenceAnalysis():
    stuffInTextFrame = someText.get("1.0", END)
    analysis = getSentenceData(stuffInTextFrame)
    # print(analysis)


root.mainloop()


# testing git 