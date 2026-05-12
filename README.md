# documenting my journey of cracking-the-coding-interview through 189-programming-questions
i'll upload/do/read/solve code/implementation/understanding/learnings from cracking-the-coding-interview-189-programming-questions-and-solutions book by Gayle Laakmann McDowell in this repo. which includes data structures, algorih, problem-solvih. ig yeah that's all :)

DAY 1 - 12th May 2026 (~ 45 mins)

Interview Question 1.1
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

My Solution/Code #1:
def isUnique(text):
    # uses additional data structure
    uniqueCharacters = {}
    for char in text:
        if char in uniqueCharacters:
            return False
        else:
            uniqueCharacters[char] = 1
    return True

My Solution/Code #2:
def isUnique(text):
    # doesn't use additional data structure
    if len(text) == 0 or len(text) == 1:
        return True
    text = sorted(text)
    for i in range( len(text) - 1 ):
        if text[i] == text[i+1]:
            return False
    return True

NOTES:
- HINT O( N.LOG(N) ) time complexity may be referring to sorting
- consider edge cases like in the solution # 2 of this problem, it has 3 edge cases (which i handled gracefully in my code 💅); empty string, singleton string, and in my implemmentation it was necessary not to run loop for the last character/index (see the code # 2 and you will know why, its OBVIOUS ma tery hi jaal ma phansa ahhh)
