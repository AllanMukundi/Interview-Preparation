"""
1.8 - Write an algorithm such that if an element in an
NxN matrix is 0, its entire row and column are set to 0.
"""

def zero_matrix(matrix):
    cols, rows = len(matrix[0]), len(matrix)
    col0 = 1
    for i in range(0, rows):
        if matrix[i][0] == 0: col0 = 0
        for j in range(1, cols):
            if (matrix[i][j] == 0):
                matrix[i][0] = 0
                matrix[0][j] = 0
        
    for i in range(rows-1, -1, -1):
        for j in range(cols-1, 0, -1):
            if (matrix[i][0] == 0) or (matrix[0][j] == 0):
                matrix[i][j] = 0
        if (col0 == 0):
            print('.')
            matrix[i][0] = 0


# Output Tests:
if __name__ == '__main__':
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(matrix)
    zero_matrix(matrix)
    print(matrix)

