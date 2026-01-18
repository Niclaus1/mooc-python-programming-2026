# Write your solution here
upper_limit = int(input('Limit:'))

current_number = 0
count = 1
string = 'The consecutive sum: '

while current_number < upper_limit:
    string += f'{count}'
    current_number += count
    count += 1
    
    if current_number < upper_limit:
        string += " + "

print(f'{string} = {current_number}')