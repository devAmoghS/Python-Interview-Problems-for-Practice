# Check if two strings are anagrams of each other

def is_anagram(str1, str2):
    # Sort all letters alphabetically, they should be equal if it is an anagram.
    return sorted(str1) == sorted(str2)

should_be_false = is_anagram('hello', 'bye')
should_be_true = is_anagram('binary', 'brainy')

print(should_be_false, should_be_true)
