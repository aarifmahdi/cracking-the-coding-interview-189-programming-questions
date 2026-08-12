# 1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

# My Solution #1:
def checkPermutation(text1, text2):
    # TC: O(N.log(N))
    # SC: O(N)
    text1 = sorted(text1)
    text2 = sorted(text2)
    if text1 == text2:
        print("They're permutations!")
    else:
        print("They're not permutations!")

# My Solution #2
def checkPermutation_improved(text1, text2):
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
