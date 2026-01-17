# Write your solution here

input_count = 0
input_total = 0
input_positive = 0
input_negative = 0

print('Please type in integer numbers. Type in 0 to finish.')
while True:
    number = int(input('Number: '))
    if number == 0:
        break
    input_count += 1
    input_total += number
    
    if number < 0:
        input_negative += 1
    else:
        input_positive += 1

input_mean = input_total / input_count

print('... the program asks for numbers')
print(f'Numbers typed in {input_count}')
print(f'The sum of the numbers is {input_total}')
print(f'The mean of the numbers is {input_mean}')
print(f'Positive numbers {input_positive}')
print(f'Negative numbers {input_negative}')

