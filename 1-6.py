# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3, If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z)

def compress(string):
    # TC: O(N)
    # SC: O(N)
    count = 0
    char = None
    l = []
    for _ in string:
        if not char:
            char = _
            count += 1
        elif _ == char:
            count += 1
        else:
            l.append(f"{char}{count}")
            char = _
            count = 1
    l.append(f"{char}{count}")
    result = "".join(l)
    if len(result) < len(string):
        return result
    return string

# test = "aabcccccaaa"
# res = compress(test)
# print(res)