# Palindrome Permutation: 
# Given a string, write a function
# to check if it is a permutation of a palindrome. 
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters. 
# The palindrome does not need to be limited to just dictionary words.

def is_permutation_of_palindrome(string):
    string = string.replace(" ", "")
    string = string.lower()
    freq = {}
    for letter in string:
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

    if len(string) % 2 == 0:
        for letter in freq:
            if freq[letter] % 2 != 0:
                return False
        return True
    else:
        if len(freq) == 1:
            return True
        else:
            odd = 0
            for letter in freq:
                if freq[letter] %2 == 0:
                    continue
                odd += 1
            if odd == 1:
                return True

    return False

# TC: O(N)
# SC: O(1)