#!/usr/bin/env python
import sys
words = []
with open("words", "r") as wordFile:
    for line in wordFile:
        line  = line[0:-1]
        words.append(line.lower())
with open("testFile", "r") as testFile:
    lineNum = 0
    for line in testFile:
        lineNum += 1
        line = line.split()
        for word in line:
            word = word.lower()
            if not(word in words):
                print(str(lineNum) + ": " + word)
