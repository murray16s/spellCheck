#!/usr/bin/env python3
import marisa_trie
import sys
words = []
sym = ["!","@","#", "$", "%", "^", "&", "*", "(", ")", "{", "}", "[", "]", "\/",".", ",", "?", "<", ">", ":", ";"]
wordFileName = sys.argv[2]
testFileName = sys.argv[1]
outFileName =  sys.argv[3]
with open(wordFileName, "r") as wordFile:
    for line in wordFile:
        line  = line[0:-1]
        words.append(line.lower())


with open(testFileName, "r") as testFile:
    with open(outFileName, "w") as outFile:
        trie = marisa_trie.Trie(words)
        lineNum = 0
        for line in testFile:
            lineNum += 1
            line = line.split()
            for word in line:
                for char in word:
                    if(char in sym):
                        word = word.replace(char, "")
                word = word.lower()
                if not(word in trie):
                    suggestions = []
                    sug = []
                    outFile.write(str(lineNum) + ": " + word + "\n")
                    for i  in range(1, len(word)-1):
                        #print("**********" + i + "**********")
                        temp = trie.keys(word[0:len(word)-i])
                        #print(temp)
                        for key in temp:
                            sug.append(key)
                        for key in sug:
                            if not(key in suggestions) and (len(suggestions) <= 10):
                                suggestions.append(key)
                    backWords = []
                    for word in words:
                        backWords.append(word[::-1])
                    trie = marisa_trie.Trie(backWords)
                    backSug = []
                    backSuggestions = []
                    for i  in range(1, len(word)-1):
                        #print("**********" + i + "**********")
                        temp = trie.keys(word[0:len(word)-i])
                        #print(temp)
                        for key in temp:
                            backSug.append(key)
                        for key in backSug:
                            if not(key in backSuggestions) and (len(backSuggestions) <= 10):
                                backSuggestions.append(key)
                    for key in backSuggestions:
                        if key not in suggestions:
                            suggestions.append(key)
                    outFile.write(str(suggestions) + "\n")
                    suggestions = []
