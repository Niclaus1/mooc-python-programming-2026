# Write your solution here
name = input('Please tell me your name:')

if name == 'Jerry':
    print('Next please!')
else:
    soup_portion = int(input('How many portions of soup?'))
    print(f'The total cost is {soup_portion * 5.90}')
    print('Next please!')
    