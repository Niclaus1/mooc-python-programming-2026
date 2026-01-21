# Write your solution here
while True:
    number = int(input('Please type in a number:'))

    if number <= 0 or number == -1:
        print('Thanks and bye!')
        break
    
    count = 1
    value = 1
    while count < number:
        value *= (count + 1) 
        count += 1

    print(f'The factorial of the number {number} is {value}')