# 1.3 URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)
# EXAMPLE
# Input: "Mr 3ohn S m i t h 13
# Output: "Mr%203ohn%20Smith"

# My Solution #1:
def URLify(text):
    # TC: O(N)
    # SC: O(N)
    arr = []
    for char in text:
        if char == " ":
            arr.append("%20")
        else:
            arr.append(char)
    return "".join(arr)

# solution#1 took 5-6 mins 

# My Solution #2
def URLify_two(char_array, true_length):
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