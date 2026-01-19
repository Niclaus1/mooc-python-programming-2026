# Write your solution here
string = input('Please type in a sting:')
stirng_len = len(string)
char = '*'
char_default = 20
char_modified = char_default - stirng_len

print(f'{char * char_modified}{string}')