# Write your solution here
from fractions import *

def fractionate(amount : int):
    fractionList = []
    for _ in range(amount):
        fractionList.append(Fraction(1, amount))
    return fractionList

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))