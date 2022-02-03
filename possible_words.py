import typing
import enchant


class PossibleWordGenerator:

    def __init__(self, **kwargs):
        self.wordStructure = kwargs.get("wordStructure")
        self.excludeLetters = kwargs.get("excludeLetters")
        self.requireLetters = kwargs.get("requireLetters")
        self.setLetterBank(self.excludeLetters)
        self.possibleWords = []
        self.initializeCurrentWord(self.wordStructure)
        self.d = enchant.Dict("en_US")
        
    def getPossibleWords(self) -> typing.List[str]:
        if self.pruneBasedOnRequiredLetters():
            return self.possibleWords

        nextLetterBlankIndex = self.findNextBlankLetterIndex()
        if nextLetterBlankIndex == -1:
            currentWord = "".join(self.currentWord)
            if self.d.check(currentWord):
                self.possibleWords.append(currentWord)
            return self.possibleWords

        for letter in self.letterBank:
            self.currentWord[nextLetterBlankIndex] = letter
            self.getPossibleWords()
            self.currentWord[nextLetterBlankIndex] = "*"

        return self.possibleWords

    def getUntouchedLetterFrequencies(self):
        frequencies = {}
        possibleWords = self.getPossibleWords()
        for untouchedLetter in self.getUntouchedLetters():
            letterUsageCount = self.getUsageCount(untouchedLetter, possibleWords)
            if letterUsageCount > 0:
                frequencies[untouchedLetter] = letterUsageCount * 1.0 / len(possibleWords)
        return frequencies

    def setLetterBank(self, excludeLetters: str):
        self.letterBank = []
        if not excludeLetters:
            self.letterBank = [c for c in alphabet]
        else:
            for letter in alphabet:
                if not letter in excludeLetters:
                    self.letterBank.append(letter)
    
    def initializeCurrentWord(self, wordStructure: str):
        self.currentWord = []
        if not wordStructure:
            self.currentWord = ["*", "*", "*", "*", "*"]
        else:
            for letter in wordStructure:
                if letter in alphabet:
                    self.currentWord.append(letter)
                else:
                    self.currentWord.append("*")

    def pruneBasedOnRequiredLetters(self):
        if not self.requireLetters:
            return False
        numBlankLetters = 0
        for letter in self.currentWord:
            if letter not in alphabet:
                numBlankLetters += 1
        numUnusedRequiredLetters = 0
        for letter in self.requireLetters:
            if letter not in self.currentWord:
                numUnusedRequiredLetters += 1
        return numUnusedRequiredLetters > numBlankLetters

    def getUntouchedLetters(self):
        untouchedLetters = []
        for letter in alphabet:
            if self.isUntouched(letter):
                untouchedLetters.append(letter)
        return untouchedLetters

    def getUsageCount(self, untouchedLetter, possibleWords):
        usageCount = 0
        for word in possibleWords:
            if untouchedLetter in word:
                usageCount += 1
        return usageCount

    def findNextBlankLetterIndex(self):
        for index, c in enumerate(self.currentWord):
            if not c in alphabet:
                return index
        return -1

    def notAlphabetLetter(self, letter):
        return not letter in alphabet

    def isUntouched(self, letter: str) -> bool:
        wordStructure = self.wordStructure if self.wordStructure else ""
        excludeLetters = self.excludeLetters if self.excludeLetters else ""
        requireLetters = self.requireLetters if self.requireLetters else ""
        return letter not in wordStructure and letter not in excludeLetters and letter not in requireLetters

    

alphabet = "abcdefghijklmnopqrstuvwxyz"