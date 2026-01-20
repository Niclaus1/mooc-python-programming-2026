# Write your solution here
word = input('Please type in a string:')
substring = input('Please type in a substring:')


index = word.find(substring)
index2 = word.find(substring, index + len(substring))

if index == -1 or index2 == -1:
    print('The substring does not occur twice in the string.')
else:
    print(f'The second occurrence of the substring is at index {index2}.')