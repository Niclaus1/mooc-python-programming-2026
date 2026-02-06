# Write your solution here
def transpose(matrix: list):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if row > col:
                ref_var = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = ref_var

if __name__ == "__main__":
    matrix = [[1,2,3],
        [4,5,6],
        [7,8,9]]

    transpose(matrix)
    for row in matrix:
        print(row)
