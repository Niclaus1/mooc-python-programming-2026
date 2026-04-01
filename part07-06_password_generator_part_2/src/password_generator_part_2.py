# Write your solution here
import string 
from random import sample,choice,shuffle

def generate_strong_password(length : int, allowNum : bool, allowSpecial : bool):
    special = "!?=+-()#"
    base = ''
    count = 0
    if allowNum and allowSpecial:
        base += ''.join(choice(string.digits))
        base += ''.join(choice(special))
        count = 2
    elif allowNum :
        base += str(choice(string.digits))
        count = 1
    elif allowSpecial:
        base += str(choice(special))
        count = 1

    if count < length:
        remaining = length - count
        password = base + ''.join(sample(string.ascii_lowercase, remaining))
        passwordList = list(password)
        shuffle(passwordList)
        return ''.join(passwordList)
    
    else:
        return base 

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(3,True,True))