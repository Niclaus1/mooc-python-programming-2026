# Write your solution here!
class NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
        self.even = 0
        self.odd = 0

    def add_number(self, number: int):
        self.numbers += number
        self.count += 1

        if number % 2 == 0:
            self.even += number
        else:
            self.odd += number

    def count_numbers(self):
        return self.count

    def get_sum(self):
        if self.count != 0:
            return self.numbers

    def average(self):
        if self.count != 0:
            mean = self.numbers / self.count
            return mean

    def count_even_numbers(self):
        return self.even

    def count_odd_numbers(self):
        return self.odd


def main():
    stats = NumberStats()
    print("Please type in integer numbers:")
    while True:
        userInput = int(input())
        if userInput == -1:
            break
        else:
            stats.add_number(userInput)
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
    print("Sum of even numbers:", stats.count_even_numbers())
    print("Sum of odd numbers:", stats.count_odd_numbers())


main()
