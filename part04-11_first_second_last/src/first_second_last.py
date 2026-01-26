# Write your solution here
def first_word(word : str):
    index = word.find(' ')
    
    return word[:index]

def second_word(word : str):
    index = word.find(' ')
    new_word = word[index + 1:]
    new_index = new_word.find(' ')
    if new_index < 0:
        return new_word
    return new_word[:new_index]

def last_word(word: str):
    words = word[::-1]
    index = words.find(' ')
    new_word = words[:index]
    
    return new_word[::-1]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))