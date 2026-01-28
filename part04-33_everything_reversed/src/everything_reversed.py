# Write your solution here
def everything_reversed(list : list):
    reversed_words = []

    for word in list:
        reversed_words.append(word[::-1])

    return reversed_words[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)