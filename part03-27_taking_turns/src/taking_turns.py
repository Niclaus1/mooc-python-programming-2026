# Write your solution here

number = int(input('Please type in a number:'))

countUp = 1
countDown = number

"""My Solution"""
while countUp < countDown:
    print(countUp)
    print(countDown)

    countUp += 1
    countDown -= 1

if number == 3:
    print(number - 1)
elif number != 3 and number % 2 != 0:
    print(number - (countUp -1))


# """Other Solution"""

# while countUp <= countDown:
#     print(countUp)

#     if countUp != countDown:
#         print(countDown)
    
#     countUp += 1
#     countDown -= 1