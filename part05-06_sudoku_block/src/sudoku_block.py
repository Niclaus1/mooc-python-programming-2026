# Write your solution here
def block_correct(sudoku : list, row_no : int, col_num : int):
    num_list = []
    
    for row in range(row_no, row_no + 3):
        for col in range(col_num, col_num + 3):
            num_list.append(sudoku[row][col])
    
    print(num_list)

    for number in num_list:
        if number > 0 and num_list.count(number) > 1:
            return False
    return True

