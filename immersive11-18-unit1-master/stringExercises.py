sudent1 = "zac"
student2 = "brandon"
student3 = "jr"
student4 = "khanh"





students = ("web class is awesome!")

print students.upper()
print students.capitalize()

print "web class is awesome!" [::-1]

leetString = "brandon hernandez"
newString = leetString.upper()
print newString.replace("A","4").replace("E","3").replace("I","1").replace("O","0").replace("S","5")

vowels = "AEIOUaeiou"
numVal = 0
vSet = set(vowels)
print vSet
rendWord = []
impWord = raw_input("Enter a word")
for letter in impWord:
    if letter in vSet:
        numVal += 1
        rendWord.append(letter)
        if numVal == 2:
            rendWord.append((letter)*3)
    else:
        numVal = 0 
        rendWord.append(letter)
wordRendered = "".join(rendWord)
print wordRendered
    

vowelDict = {
    "a": "aaaa",
    "e": "eeee",
    "i": "iiii",
    "o": "oooo",
    "u": "uuuu",
}
longVowelStr = ""
for i in range(0,len(impWord)):
    currentLetter = impWord[i]
    nextLetter = impWord[i+1]
    if((currentLetter == nextLetter) and (i != len(impWord)-1)):
        if(currentLetter in vowelDict):
            currentLetter = vowelDict[currentLetter]
    longVowelStr += currentLetter
print longVowelStr





