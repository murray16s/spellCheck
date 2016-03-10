#!/usr/bin/env python
import sys
words = []
wordFileName = sys.argv[2]
testFileName = sys.argv[1]
with open(wordFileName, "r") as wordFile:
    for line in wordFile:
        line  = line[0:-1]
        words.append(line.lower())
with open(testFileName, "r") as testFile:
    lineNum = 0
    for line in testFile:
        lineNum += 1
        line = line.split()
        for word in line:
            word = word.lower()
            if not(word in words):
                print(str(lineNum) + ": " + word)
