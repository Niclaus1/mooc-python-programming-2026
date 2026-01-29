# Write your solution here
def longest_series_of_neighbours(list : list):
    diff_list = []
    prev_num = list[0]
    count = 0

    for number in list:
        difference = number - prev_num

        if difference == -1:
            difference = 1

        diff_list.append(difference)
        prev_num = number

    final_count = []
    for diff in diff_list:

        if diff == 1 or diff == int(-1):
            count += 1

        else:
            final_count.append(count)
            count = 0

        final_count.append(count)

    return max(final_count) + 1

if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 23, 24, 25]
    print(longest_series_of_neighbours(my_list))

