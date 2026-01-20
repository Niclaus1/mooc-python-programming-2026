# Write your solution here
word = input('Please type in a word:')
character = input('Please type in a character:')
index = word.find(character)

if len(word) < 3:
    print()
elif index == -1:
    print()
elif (index + 3) > len(word):
    print()
else:
    print(word[index : index + 3])
    