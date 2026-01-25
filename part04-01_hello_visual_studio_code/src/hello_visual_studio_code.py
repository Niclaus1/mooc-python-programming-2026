# Write your solution here

while True:
    word = input('Editor:')
    if word.lower() == 'visual studio code':
        print('an excellent choice!')
        break
    elif word.lower() == 'vim' or word.lower() == 'word' or word.lower() == 'notepad':
        print('awful')
    else:
        print('not good')   