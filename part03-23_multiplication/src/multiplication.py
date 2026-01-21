# Write your solution here
number = int(input('Please type in a number:'))

count = 1
while count < (number + 1):
    step = 1
    
    while step < (number + 1):
        print(f'{count} x {step} = {count * step}')
        step += 1
        
    count += 1