"""
1.7 - Given an image represented by an NxN matrix,
where each pixel in the image is 4 bytes, write a
method to rotate the image by 90deg. Can you do this
in place?
"""

def rotate(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n-layer-1
        for i in range(first, last):
            top = (first, i)
            right = (i+0, last)
            left = (n-i-1, layer)
            bottom = (last, n-i-1)
            # top element
            temp = matrix[top[0]][top[1]]
            # left -> top
            matrix[top[0]][top[1]] = matrix[left[0]][left[1]]
            # bottom -> left
            matrix[left[0]][left[1]] = matrix[bottom[0]][bottom[1]]
            # right -> bottom
            matrix[bottom[0]][bottom[1]] = matrix[right[0]][right[1]]
            # top -> right
            matrix[right[0]][right[1]] = temp


# Output Tests:
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(matrix)
rotate(matrix)
print(matrix)

