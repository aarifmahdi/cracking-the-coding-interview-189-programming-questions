# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.


def setZeroes(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # TC: O(M*N)
        # SC: O(M+N)
        target_rows = set()
        target_columns = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    target_rows.add(i)
                    target_columns.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in target_rows:
                    matrix[i][j] = 0
                if j in target_columns:
                    matrix[i][j] = 0


# solved on leetcode: "73. Set Matrix Zeroes"