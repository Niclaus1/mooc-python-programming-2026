# write your solution here
def matrix_sum():
    with open('matrix.txt') as new_file:
        row_sum = []
        for line in new_file:
            line = line.replace('\n', "")
            numbers = line.split(',')
            row_sum.append(sum(numbers))

        return sum(row_sum)

def matrix_max():
    with open('matrix.txt') as new_file:
        highest = 0
        
        for line in new_file:
            line = line.replace('\n', "")
            numbers = line.split(',')
            for number in numbers:
                number = int(number)
                if highest < number:
                    highest = number
        return highest

def sum(row_num : list):
    value = 0
    for row in row_num:
        value += int(row)
    return value

def row_sums():
    with open('matrix.txt') as new_file:
        num_list = []
        for line in new_file:
            line = line.replace('\n', "")
            row_num = line.split(',')
            
            num_list.append(sum(row_num))
        return num_list

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())