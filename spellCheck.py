#!/usr/bin/env python3
import marisa_trie
import sys
words = []
sym = ["!","@","#", "$", "%", "^", "&", "*", "(", ")", "{", "}", "[", "]", "\/",".", ",", "?", "<", ">", ":", ";"]
wordFileName = sys.argv[2]
testFileName = sys.argv[1]
with open(wordFileName, "r") as wordFile:
    for line in wordFile:
        line  = line[0:-1]
        words.append(line.lower())
trie = marisa_trie.Trie(words)
suggestions = []
sug = []
with open(testFileName, "r") as testFile:
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
                print(str(lineNum) + ": " + word)
                for i  in range(1, len(word)-1):
                    #print("**********" + i + "**********")
                    temp = trie.keys(word[0:len(word)-i])
                    #print(temp)
                    for key in temp:
                        sug.append(key)
                    for key in sug:
                        if not(key in suggestions) and (len(suggestions) <= 10):
                            suggestions.append(key)
                print(suggestions)
