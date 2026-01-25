# Copy here code of line function from previous exercise
def line(number, string):
    row = 1
    
    while row < number + 1:
        print(string * row)
        row += 1
        
        
def triangle(size):
    # You should call function line here with proper parameters
    line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
