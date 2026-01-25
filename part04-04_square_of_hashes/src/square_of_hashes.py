# Copy here code of line function from previous exercise
def line(number, string):
    row = 0
    
    while row < number:
        col = 0
        
        while col < number:
            print(string, end="")

            col += 1
        print()
        row += 1

def square_of_hashes(size):
    # You should call function line here with proper parameters
    line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
