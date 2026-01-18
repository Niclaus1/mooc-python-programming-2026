# Write your solution here
upper_limit = int(input('Limit:'))

current_number = 0
count = 1

while current_number < upper_limit:
    current_number += count
    count += 1  
print(current_number)