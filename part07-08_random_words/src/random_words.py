# Write your solution here
from random import sample

def words(n:int, beginning:str):
    wordMatch = []
    with open('words.txt') as file:
        for line in file:
            line = line.strip()
            if line.startswith(beginning):
                wordMatch.append(line)
    
    return sample(wordMatch,n)

if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)