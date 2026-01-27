# Write your solution here
def length_of_longest(list : list):
    longest_length = []

    for word in list:
        longest_length.append(len(word))

    return max(longest_length)

if __name__ == "__main___":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)