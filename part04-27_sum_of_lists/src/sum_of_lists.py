# Write your solution here
def list_sum(listA : list, listB: list):
    sum_value = []
    
    index = 0
    while index < len(listA):
        index_sum = listA[index] + listB[index]
        
        sum_value.append(index_sum)
        index += 1
    return sum_value

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))