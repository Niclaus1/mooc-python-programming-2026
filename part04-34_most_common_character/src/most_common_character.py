# Write your solution here
def most_common_character(word : str):

    previous_max = word[0]

    for char in word:
        if word.count(char) > word.count(previous_max):
            previous_max = char

    return previous_max

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
