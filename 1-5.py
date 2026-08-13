# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# p a l e , p l e - > t r u e
# p a l e s , p a l e - > t r u e
# p a l e , b a l e - > t r u e
# p a l e , b a k e - > f a l s e


def is_one_edit_away(s1, s2):
    # TC: O(N)
    # SC: O(1)
    if s1 == s2:
        return True
    if len(s1) == len(s2):
        mismatch_count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                mismatch_count += 1
        if mismatch_count > 1:
            return False
        return True
    if abs(len(s1) - len(s2)) == 1:
        big=None 
        tiny=None
        if len(s1) > len(s2):
            big = s1
            tiny = s2
        else:
            big = s2
            tiny = s1
        mismatch = False
        i=0
        j=0
        while i < len(tiny):
            if tiny[i] != big[j] and not mismatch:
                mismatch = True
                j+=1
                continue
            if tiny[i] == big[j]:
                i += 1
                j += 1
                continue
            else:
                return False
        return True
    return False