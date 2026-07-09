import random


# Write your solution here:
def word_generator(characters: str, length: int, amount: int):
    for _ in range(amount):
        yield "".join(random.sample(characters, k=length))


if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)
