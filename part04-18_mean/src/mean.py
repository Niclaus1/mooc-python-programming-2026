# Write your solution here
def mean(list: list):
    count = len(list)
    
    value = 0
    index = 0
    
    while index < count:
        value += list[index]
        index += 1
    return value / count

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = mean(my_list)
    print(result)