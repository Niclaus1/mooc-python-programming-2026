# Write your solution here
correct_password = '4321'
attempt = 1
while True:
    input_password = input('PIN:')
    if input_password == correct_password:
        if attempt == 1:
            print('Correct! It only took you one single attempt!')
            break
        print(f'Correct! It took you {attempt} attempts')
        break
    else:
        print('Wrong')
        attempt += 1
        