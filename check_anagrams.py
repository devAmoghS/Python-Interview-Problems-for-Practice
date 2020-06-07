# Problem: Two strings of sizes m and n are given,
# we have to find how many characters need to be
# removed from both the string so that they become
# anagrams of each other

# Anagrams: Words that are made from rearranging the letters of another word

# Algorithm: We will use dictionaries to keep track of characters. 
# The idea is to get the common occuring characters and derive 
# uncommon characters

import string

# letters will be a string of the form "abc...xyz"
# CHARACTER_HASH looks like this {'a'0, 'b':0 ...., 'z':0}
letters = string.ascii_lowercase
CHARACTER_HASH = dict(zip(letters, [0] * len(letters)))


# This method will mark all the letters occuring in 'text_a'
def mapLettersToHash(text_a):
    for char in text_a:
        if char in CHARACTER_HASH.keys():
            CHARACTER_HASH[char] += 1


# This method will count the letters present in 'text_b', also found in 'text_a'
# These will be charcaters whose frequency in HASH is greater than zero
def computeCommonLetters(text_b):
    common_letters = 0
    for char in text_b:
        if CHARACTER_HASH[char] > 0:
            common_letters += 1
    return common_letters


# Now we derive how many uncommon letters are present,
# This is done by subtracting twice the count of common letters
# from the total length of both the strings
def computeUncommonLetters(text_a, text_b, common_letters):
    return abs(len(text_a) + len(text_b) - (2 * common_letters))

if __name__ == "__main__":
    text_1 = "hello"
    text_2 = "billion"

    mapLettersToHash(text_1)
    common = computeCommonLetters(text_2)
    result = computeUncommonLetters(text_1, text_2, common)
    print(result)
