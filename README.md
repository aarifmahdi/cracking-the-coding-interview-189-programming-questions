# documenting my journey of cracking-the-coding-interview through 189-programming-questions
i'll upload/do/read/solve code/implementation/understanding/learnings from cracking-the-coding-interview-189-programming-questions-and-solutions book by Gayle Laakmann McDowell in this repo. which includes data structures, algorih, problem-solvih. ig yeah that's all :)

DAY 1 - 13th May 2026 (~ 45 mins)

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


DAY 2 - 14th May 2026 (~ 50 mins)

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


DAY 3 - 15TH MAY 2026 (~ 50mins)

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


DAY 4 - 16th MAY 2026 (~ 10mins)

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
            arr.append("%20")
        else:
            arr.append(char)
    return "".join(arr)

*it took only 5-6 mins to solve this
*i only wrote the code (cuz cousin aya ha toh just wanted to mark the day atleast), didn't work on TC,SC analysis, nor looked for optimized solutions

for day5, analyze this for TC,SC and see optimized solutions (see TC,SC of list's append() and string's join() method)


DAY 5 - 17th MAY 2026 (~ 40mins)

Python's string's join() method -> str.join()

- The time complexity of Python's str.join() method is O(n), where (n) is the total length of the resulting string.
- Specifically, if you are joining (k) strings with a total character count of L and a separator of length s, the complexity is O(L + k*s) ; actually (k-1) * s cuz join doesn't add the separator on last string
- vs concatenation: 
string += new_str (in a loop), it's O(n^2) i.e. Quadratic cuz repeatedly loop ma concatenate krta krta

*join() is highly optimized:
- Two-Pass Process: Python first iterates through the iterable to calculate the total required length of the final string (like this -> list ma loop chalaya, elements saaray string hain, loop ki har iteration ma it gets the length of string (i.e. element of list), and sums up on every iteration to get total required length/size for resulting string. this is my thinking ky aesa hota hoga)
- Single Allocation: It allocates memory for the entire resulting string once.
- Memory Copying: It then performs a second pass to copy each substring directly into the pre-allocated memory block.

SC:  Because the size of the allocated memory grows proportionally with the total length of the input strings and the separator, the space complexity remains O(n)

so in conclusion,
- str.join() TC & SC: O(N)
& concatenation in loop is O(N^2) (SC: O(N))

Python's list's append method -> list.append()

- The time complexity of appending an item to a list in Python is O(1) amortized.
- While most appends are instantaneous, Python must occasionally resize the list's underlying memory, which takes O(n) time. However, because this happens infrequently, the average time per operation remains constant.
- Amortized (Average) O(1) Most calls
- Worst Case (Resizing, explained below 👇) O(n) When list is full

SC: O(1) (Adds one element)

👇RESIZING of Python's list -> O(N)

Formula: It generally grows by roughly 12.5% (1/8th) plus a small constant for larger lists
Small List Growth: For a new list, the capacity jumps in steps like: 0, 4, 8, 16, 24, 32, 40, 52, 64, 76....

HOW RESIZING WORKS?
- Python lists are implemented as dynamic arrays
- Over-allocation: To keep appends fast, Python allocates more space than currently needed.
- Constant Time: If there is free space at the end of the array, append() simply places the object there.
- Resizing: When the allocated space is full, Python creates a new, larger array and copies all existing elements to it (this copying of all elements into new array takes O(N) time, which is understandable)

for interviews take append() as O(1)
👆!!! DO CONFIRM THIS !!!

did the analysis of my solution #1 for problem 1.3:
- TC: O(N)
- SC: O(N)


for day6, see the optimized solution(s) for this problem 1.3 (remaining 6 problems 1.4-1.9 of Chapter1 Arrays & Strings, WILL DO THESE LATER, after doing Chapter 2,3)
if time allows, do 2.1 (linked lists chapter)


DAY 6 - 18th MAY 2026 (~ 55mins)

*understood hint #53 (given by the author) and implemented the solution based on it.
*actually the question said, You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.
- true length: size of string containing characters (excluding the extra spaces at the end)
- sufficient space: extra spaces included at the end of string (string means array of characters truly, as in C++)
question also said, Note: If implementing in Java, please use a character array so that you can perform this operation in place (so i simulated/mimicked the same concept in Python
 
👇for problem 1.3
My Solution #2
def URLify(char_array, true_length):
    # implements hint #53
    num_space = 0
    for i in range(true_length):
        if char_array[i] == " ":
            num_space += 1
    write_index = (true_length + (num_space * 2)) - 1
    for i in range(true_length - 1, -1, -1):
        if char_array[i] == " ":
            char_array[write_index] = '0'
            char_array[write_index - 1] = '2'
            char_array[write_index - 2] = '%'
            write_index -= 3
        else:
            char_array[write_index] = char_array[i]
            write_index -= 1
    return

slicing in Python TC and SC: O(N)
because it has to traverse the string to copy the characters + it creates a new list in-memory for this purpose.

for day7, see hint #0118 solution, is that more optimized than hint #53?

DAY 7 - 19th May 2026 (~ mins)

- hint #0118 refers to calculating the number of spaces in input string (which we already did in solution #2 so its already utilized)

{
AS PLANNED, remaining 6 problems 1.4-1.9 of Chapter1 Arrays & Strings, WILL DO THESE LATER, after doing Chapter 2,3
}

2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

wrote first draft/solution of 2.1 but it has bugs/issues (see Google's AI mode chat tmrw to learn n do it properly for interviews)
