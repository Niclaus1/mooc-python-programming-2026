# Write your solution here
import string 
from random import sample

def generate_password(length : int):
    return ''.join(sample(string.ascii_lowercase,length))

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))