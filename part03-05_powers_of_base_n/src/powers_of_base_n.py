# Write your solution here
upper_limit = int(input('Upper limit:'))
base = int(input('Base:'))

current_number = 1

while current_number <= upper_limit:
    print(current_number)

    current_number *= base
    