# Write your solution here

number = int(input('Please type in a number:'))

count = 2
while count <= number:
    
    
    print(count)
    
    step = 0
    while step < (count - 1):
        step += 1
        
    print(step)
    count += 2
    
if number % 2 != 0:
    print(count - 1)