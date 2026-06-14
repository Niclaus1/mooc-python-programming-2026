# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    wordList = [word for word in string]
    return "".join([char for char in wordList if char not in forbidden])


if __name__ == "__main__":
    sentence = "Once! upon, a time: there was a python!??!?!"
    filtered = filter_forbidden(sentence, "!?:,.")
    print(filtered)
