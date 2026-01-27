# Write your solution here
def distinct_numbers(list: list):
    distint_list = []

    for i in list:

        if i in distint_list:
            continue
        else:
            distint_list.append(i)

    return sorted(distint_list)

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]