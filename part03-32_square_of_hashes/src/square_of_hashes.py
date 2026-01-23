# Write your solution here
def hash_square(count):
    char = "#"
    step = 0
    
    while step < count:
        print(char * count)
        step += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)