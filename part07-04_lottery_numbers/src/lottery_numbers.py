# Write your solution here
from random import sample

def lottery_numbers(amount : int, lower : int, upper :int):
    number_pool = list(range(lower, upper))
    lot_num = sample(number_pool,amount)
    
    return sorted(lot_num)
if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)