# Write your solution here
number_input = int(input('Please type in a number:'))

absolute_val = 0
if number_input < 0:
    absolute_val = number_input * -1
else:
    absolute_val = number_input

print(f'The absolute value of this number is {absolute_val}')