# Write your solution here
def spruce(number):
    row = 1
    
    space = ' '
    char = '*'
    
    print('a spruce!')
    while row < number + 1:
        spaces = space * (number - row)
        stars = char * (2 * row - 1)
        
        print(spaces + stars)
        row += 1

    print(space * (number - 2), char)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)