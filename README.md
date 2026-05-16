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
    # doesn't use additional data structure    !!! THIS WAS A MISTAKE - read line #47-48!!!
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
- hint # 2 referred to a solution using "bit vector", i don't have knowledge on this topic, tried youtube, built basic understanding of a bit vector, but didn't think how to use it for this problem (due to time constraint, 45 mins se zyada nhi spend krunga until finals/exams to maintain consistency cuz DISCIPLINE >> MOTIVATION ahhh words)

for day 2 : learn and implement solution of problem 1.1 using hint # 2. if time allows do next problem as well (1.2)


DAY 2 - 13th May 2026 (~ 50 mins)

NOTES:
- Performed analysis for time complexity and space complexity of solution #1 and solution #2. For #1 TC = O(N) and SC = O(N).
- At first i thought it should be O(1) for both cuz characters are limited (alphabets -> 26 characters, ascii -> 128 or 256 characters (7-bit or 8-bit encoding), unicode characters also limited) so it should be considered constant right? And since the code runs for maximum characters in the worst case its also constant? but NAHHH, for interviews you can't assume the characters are limited, just assume that its arbitrarily infinite like the input string.
- N <= C (N is the input string and C is the character set size means kitny characters maximum hain) and for this problem N <= C bcz at (C+1)th character u encounter a duplicate value, where loop breaks.
- therefore the big-O notation truly is O(min(N,C)) which boils down to O(N). i understand this part how O(min(N,C)) is O(N) for simplicity, but don't ask me pls 🙂.
- text = sorted(text) THIS IS USING AN ADDITIONAL DATA STRUCTURE!!!
- sorted() uses a list data structure (timsort, the python algorithm for sorting does this) so when u use sorted() its using an additional data structure
- For #2 TC = O(N.LOG(N)) and SC = O(N). sorting takes O(N.LOG(N)) time. SC has same logic as solution # 1
- also saw how boolean arrrays can be used to solve this problem but that also takes O(N) for TC and SC so didn't bother to implement it.

i guess that's all, couldn't get the time to see bit vector thing.
for day 3, do the problem 1.2 (will see the bit vector thing after exams/finals)


DAY 3 - 14TH MAY 2026 (~ 50mins)

1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.

My Solution #1:
def checkPermutation(text1, text2):
    # TC: O(N.log(N))
    # SC: O(N)
    text1 = sorted(text1)
    text2 = sorted(text2)
    if text1 == text2:
        print("They're permutations!")
    else:
        print("They're not permutations!")

My Solution #2
def checkPermutation(text1, text2):
    # TC: O(N)
    # SC: O(N)
    if len(text1) != len(text2):
        print("They're not permutations!")
        return
    freq = {}
    for i in range(len(text1)):
        if text1[i] in freq:
            freq[text1[i]] += 1
        else:
            freq[text1[i]] = 1
        if text2[i] in freq:
            freq[text2[i]] -= 1
        else:
            freq[text2[i]] = -1
    for key in freq:
        if freq[key] != 0:
            print("They're not permutations!")
            return
    print("They're permutations!")

NOTES:
- Ask for the definition of terms used in question/problem statement. for eg: i couldn't recall what permutation meant, so i searched it up.
- permutation: two strings have exact same characters arranged in different order (so they must have same length); eg: "abc" "cba"
- The BEST and most OPTIMIZED solution for this problem is My Solution #2
- But it can also be a solution with SC: O(1) i.e. constant space complexity, when it is given that the character set is limited (eg: ASCII only). A fixed-size array can be used to achieve O(1) SC in this specific case.

ig this is all of today's learnings, for day 4, solve problem 1.3


DAY 4 - 15th MAY 2026

1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr 3ohn S m i t h 13
Output: "Mr%203ohn%20Smith"

My Solution #1:
def URLify(text):
    arr = []
    for char in text:
        if char == " ":
            arr.append("")
        else:
            arr.append(char)
    return "".join(arr)

*it took only 5-6 mins to solve this
*i only wrote the code (cuz cousin aya ha toh just wanted to mark the day atleast), didn't work on TC,SC analysis, nor looked for optimized solutions

for day5, analyze this for TC,SC and see optimized solutions (see TC,SC of list's append() and string's join() method)
