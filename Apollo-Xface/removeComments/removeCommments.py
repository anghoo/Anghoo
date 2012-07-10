"""
    Goal:
    1. copy all non-java sources to targetDir
    2. remove all comments from source files
    3. make targetDir have same structure with srcDir
"""

import re
import os

def removeCommentsInString(string):
    # remove all occurrence streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("/\*.*?\*/", re.DOTALL) , "" , string)
    # remove all occurrence single line comments (//COMMENT\n ) from string
    string = re.sub(re.compile("//.*?\n") , "" , string)
    return string

def readFileAsString(filePath):
    file = open(filePath, 'r')
    return file.read()
