#Following along with teacher. 

#Uppercase string
aString = "brian";
print aString.upper()

#Capitlize a string
print aString.capitalize()

#Reverse a string
print aString[::-1]
#Other method
aStringAsAList = list(aString)
aStringAsAList.reverse()
print ''.join(aStringAsAList)

#LeetSpeak
leetString = "Brian Lafuente"
newString = leetString.upper()
# print newString.replace("A", "4").replace("E", "3").replace("G", "6").replace("I", "1").replace("O", "0").replace("S", "5").replace("T", "7")

leetDict = {
    "A": "4",
    "E": "3",
    "G": "6",
    "I": "1",
    "O": "0",
    "S": "5",
    "T": "7"
}
finalString = ""
for i in range(0, len(newString)):
    currentLetter = newString[i]
    # print currentLetter
    if(currentLetter in leetDict):
        currentLetter = leetDict[currentLetter]
    finalString += currentLetter
print finalString

#Long-long Vowels
vowels = "AEIOUaeiou"
numVal = 0 
vSet = set(vowels)
rendWord = []
impWord = raw_input("Enter a word: ")
for i in impWord:
    if i in vSet:
        numVal += 1
        rendWord.append(i)
        if numVal == 2:
            rendWord.append((i) * 5)
    else:
        numVal = 0
        rendWord.append(i)
wordRendered = "".join(rendWord)
print wordRendered

#Another method
vowelDict = {
    "a": "aaaaa",
    "e": "eeeee",
    "i": "iiiii",
    "o": "ooooo",
    "u": "uuuuu"
}
longVowelStr = ""
for i in range(0,len(impWord)):
    currentLetter = impWord[i]
    nextLetter = impWord[i+1]
    if(currentLetter == nextLetter) and (i != len(impWord) -i):
        if(currentLetter in vowelDict):
            currentLetter = vowelDict[currentLetter]
    longVowelStr += currentLetter
print longVowelStr
    