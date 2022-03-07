# A pangram is a sentence that contains every single letter of the alphabet 
# at least once. For example, the sentence "The quick brown fox jumps over
#  the lazy dog" is a pangram, because it uses the letters A-Z at least once 
#  (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is,
#  False if not. Ignore numbers and punctuation.

def is_panagram(s):
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' , 'y', 'z']
    for letter in alphabet_list:
        if letter not in s.lower():
            return False
    return True

print(is_panagram("The quick brown fox jumps over the lazy dog"))

