# Write your solution here
word = input('Please type in a word:')
character = input('Please type in a character:')

while True:
    index = word.find(character)
    
    if len(word) < 3:
        break
    elif index == -1:
        break
    elif (index + 3) > len(word):
        break
    
    print(word[index: index + 3])
    word = word[index + 1:]
