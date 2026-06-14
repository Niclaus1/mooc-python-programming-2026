# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    with open(filename, "r") as file:
        clean_List = [
            word.replace(",", "").replace(".", "") for word in file.read().split()
        ]
        unique_word = set(clean_List)
        print(clean_List)
        return {
            word: clean_List.count(word)
            for word in unique_word
            if clean_List.count(word) >= lower_limit
        }


if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))
