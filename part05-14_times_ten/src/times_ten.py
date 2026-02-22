# Write your solution here
def times_ten(start_index: int, end_index: int):
    dict = {}
    for x in range(start_index, end_index + 1):
        dict[x] = x * 10
    return dict

if __name__ == "__main__":
    print(times_ten(1,3))
