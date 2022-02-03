import typing
import collections
import word_list

def getNovelLetters(openingWord: str, nextWords: typing.List[str]) -> typing.Dict[str, typing.List[str]]:
    novelLettersToWords = collections.defaultdict(list)
    for word in nextWords:
        novelLetters = ""
        for letter in word:
            if not letter in openingWord and not letter in novelLetters:
                novelLetters += letter
        alphabetizedNovelLetters = "".join(sorted(novelLetters))
        novelLettersToWords[alphabetizedNovelLetters].append(word)
    return novelLettersToWords

def main():
    print(getNovelLetters("soare", word_list.shortWordList))
    print(getNovelLetters("soare", word_list.wordList))

if __name__ == "__main__":
    main()