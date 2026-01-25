# Copy here code of line function from previous exercise
def line(number, string):
    count = 0
    
    while count < number:
        print(string * 10)
        count += 1
    
def box_of_hashes(height):
    # You should call function line here with proper parameters
    line(height, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
