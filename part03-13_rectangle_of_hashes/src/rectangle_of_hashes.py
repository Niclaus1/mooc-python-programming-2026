# Write your solution here
width = int(input('Width:'))
height = int(input('Height:'))
count = 0
string = '#'

while count < height:
    print(string * width)
    count += 1