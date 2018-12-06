import re

sampleText =  "The any development[Nominalization] of this any machine began in 1834 , which helped lead to the adoption of a punched card system that was derived from the Jacquard loom.the loom was long used in many applications.and then we left. Her house was large.but not so large we couldn't stay.we did."

testString = sampleText
newString = testString.replace(" , ", ", ")
evenNewerString = newString.replace(".", ". ")

pattern = re.compile(r'\.[a-z]')


# def matches():
#     pattern = re.compile(r'(\s,\s|\.[a-z])')
#
#     matches = pattern.finditer(sampleText)
#
#     for match in matches:
#         print(match.group())



# Sub method is particular to regular expression module.


def changeToUpperCase(matchObject):
    period, letter = matchObject.group() # Returns a tuple of the matched elements
    return f"{period} {letter.upper()}" # Puts a space after the period and capitalizes the letter after it.

def createSpaceAfterPeriods(text):
    patternForPeriod = re.compile(r'\.[a-z]') # Pattern to match
    output = patternForPeriod.sub(changeToUpperCase, text) # substitutes the pattern found with what's returned from the function changeToUpperCase.
    return output

# print(replacesSpacesNearCommas(sampleText))


# def upping(match):
#     dot, letter = list(match.group())
#     print("This is the match.group value:", match.group())
#     print("This is the match.group value in a list:", list(match.group()))
#     return f"{dot} {letter.upper()}"


patternforperiods = re.compile(r"(\.[a-z])")
# print(patternforperiods.sub(upping, sampleText))


# print(replacesSpacesNearCommas(sampleText))




# print(newString)
# print(evenNewerString)
# print(matches())


#
# r"(\.[a-z])
#
# .{lowercaseletterswithoutspace}