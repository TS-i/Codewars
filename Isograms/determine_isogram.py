# Goal - 
# An isogram is a word that has no repeating
# letters, consecutive or non-consecutive. 
# Implement a function that determines 
# whether a string that contains only letters
# is an isogram. Assume the empty string is 
# an isogram. Ignore letter case.

# Given Code -
# def is_isogram(string):
    #your code here

# Solution -
def is_isogram(string):
    string = string.lower()
    return len(set(string)) == len(string)