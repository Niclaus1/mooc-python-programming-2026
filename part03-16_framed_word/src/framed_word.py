# Write your solution here
word = input('Word:')
char = '*'
space = ' '

word_len = len(word)
space_need = (28 - word_len) // 2

if word_len % 2 == 0:
    print(char * 30)
    print(f'{char}{space * space_need}{word}{space * space_need}{char}')
    print(char * 30)
else:
    print(char * 30)
    print(f'{char}{space * space_need}{word}{space * (space_need + 1)}{char}')
    print(char * 30)
    
