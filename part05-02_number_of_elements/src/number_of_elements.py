# Write your solution here
def count_matching_elements(my_matrix : list, element: int):
    
    count = 0
    my_list = my_matrix
    
    for row in range(len(my_list)):
        
        for col in range(len(my_list[row])):
            if my_matrix[row][col] == element:
                count += 1
    return count

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))