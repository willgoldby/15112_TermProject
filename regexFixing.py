import re

def changeToUpperCase(matchObject):
    '''Returns changes to text that are called from .sub method for regular expressions in other function.'''
    period, letter = matchObject.group() # Returns a tuple of the matched elements.
    return f"{period} {letter.upper()}" # Puts a space after the period and capitalizes the letter after it.

def createSpaceAfterPeriods(text):
    '''Returns text that has a space and capital letter after periods.'''
    patternForPeriod = re.compile(r'\.[a-zA-Z]') # Pattern to match
    output = patternForPeriod.sub(changeToUpperCase, text) # substitutes the pattern found with what's returned from the function changeToUpperCase.
    return output


def removeSpaces(matchObject):
    '''Returns changes to text that are called from .sub method for regular expressions in other function.'''
    space1, comma, space2 = matchObject.group()  # Returns a tuple of the matched elements.
    return f"{comma} "

def removeSpacesAroundCommas(text):
    '''Returns text that removes inappropriate spaces around commas.'''
    patternforSpaces = re.compile(r'\s,\s')
    output = patternforSpaces.sub(removeSpaces, text)
    return output

def fixErrors(text):
    '''Returns text that has a space and capital letter after period as well as correct spacing around coommas.'''
    fixUppercasing = createSpaceAfterPeriods(text)
    fixSpacing = removeSpacesAroundCommas(fixUppercasing)
    finalOutput = fixSpacing
    return finalOutput