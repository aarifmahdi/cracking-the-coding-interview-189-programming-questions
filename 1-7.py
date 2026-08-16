# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rotate_image(matrix: list) -> list:
    # TC: O(N^2)
    # SC: O(N^2)
    result = [["0" for i in range(len(matrix))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        offset = 0
        for j in range(len(matrix)):
            result[offset][-(i+1)] = matrix[i][j]
            offset += 1
    return result


matrix = [[1,2,3],[4,5,6],[7,8,9]]