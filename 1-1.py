# 1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

def isUnique(text):
    # TC: O(N)
    # SC: O(N)
    # uses additional data structure
    uniqueCharacters = {}
    for char in text:
        if char in uniqueCharacters:
            return False
        else:
            uniqueCharacters[char] = 1
    return True

# My Solution/Code #2:
def isUnique_two(text):
    # TC: O(N.log(N))
    # SC: O(N)
    # uses additional data structure
    if len(text) == 0 or len(text) == 1:
        return True
    text = sorted(text)
    for i in range( len(text) - 1 ):
        if text[i] == text[i+1]:
            return False
    return True
