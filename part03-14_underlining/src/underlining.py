# Write your solution here


while True:
    string = input('Please type in a string:')
    string_len = len(string)
    dash = '-'
    print()
    
    if len(string) <= 0:
        break
    else:
        print(string)
        print(string_len * dash)
    print()