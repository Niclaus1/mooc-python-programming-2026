# Write your solution here
def all_the_longest(list : list):

    longest_words_list = []
    len_of_words = []
    
    for word in list:
        len_of_words.append(len(word))

    max_len = max(len_of_words)

    for word in list:
        if len(word) == max_len:
            longest_words_list.append(word)

    return longest_words_list

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result) # ['eleventh']