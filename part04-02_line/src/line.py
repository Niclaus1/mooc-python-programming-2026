# Write your solution here
def line(number, string):
    count = 0
    while count < number:
        if string == "":
            print('*' ,end="")
            count += 1
        else:
            print(string[0], end="")
            count += 1
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "")