# Write your solution here

def greatest_number(a: int, b: int ,c: int):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif a == b and b == c:
        return a
    else:
        return c
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(1, 1, -100)
    print(greatest)
    