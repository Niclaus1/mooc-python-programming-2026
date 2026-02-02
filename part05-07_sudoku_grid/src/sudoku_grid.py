# Write your solution here
def sudoku_grid_correct(sudoku: list):
    status = []
    for line in range(len(sudoku)):
        status.append(row_correct(sudoku,line))
        status.append(column_correct(sudoku, line))
            
    for row in range(0,len(sudoku), 3):
        for col in range(0,len(sudoku), 3):
            status.append(block_correct(sudoku,row,col))
    
    if False in status:
        return False
    return True
    
def row_correct(sudoku: list, row_no : int):
    
    row_count = []
    for col in range(1, len(sudoku)):
        row_count.append(sudoku[row_no].count(col))

    for count in row_count:
        if count > 1:
            return False
    return True

def column_correct(sudoku: list, column_no: int):

    col_count = []
    for row in range(len(sudoku)):
        col_count.append(sudoku[row][column_no])
    
    for duplicate in col_count:
        if duplicate > 0 and col_count.count(duplicate) > 1:
            return False
    return True

def block_correct(sudoku : list, row_no : int, col_num : int):
    num_list = []
    
    for row in range(row_no, row_no + 3):
        for col in range(col_num, col_num + 3):
            num_list.append(sudoku[row][col])

    for number in num_list:
        if number > 0 and num_list.count(number) > 1:
            return False
    return True

if __name__ == "__main__":

    sudoku = [
        [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
        [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
        [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
        [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
        [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
        [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
        [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
        [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
        [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
        ]

    print(sudoku_grid_correct(sudoku))