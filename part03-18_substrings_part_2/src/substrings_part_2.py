# Write your solution here
word = input('Please type in a string:')

count = len(word)

while count >= 0:
    print(word[count:len(word)])
    count -= 1
