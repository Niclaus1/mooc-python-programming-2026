# Write your solution here
def row_correct(sudoku: list, row_no : int):
    
    row_count = []
    for col in range(1, len(sudoku)):
        row_count.append(sudoku[row_no].count(col))

    for count in row_count:
        if count > 1:
            return False
    return True
