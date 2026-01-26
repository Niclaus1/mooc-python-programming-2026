# Write your solution here
numbers = [1, 2, 3, 4, 5]

while True:
    index = int(input('Index:'))
    
    if index < 0:
        break
    
    number = int(input('New value:'))

    numbers[index] = number
    print(numbers)