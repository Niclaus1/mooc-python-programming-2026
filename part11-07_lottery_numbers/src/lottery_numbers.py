# WRITE YOUR SOLUTION HERE:
# ruff: noqa: E201
class LotteryNumbers:
    def __init__(self, week: int, numbers: list):
        self._week = week
        self._numbers = numbers

    def number_of_hits(self, number_call: list):
        return len([number for number in number_call if number in self._numbers])

    # fmt: off
    def hits_in_place(self, numbers: list):
        return [number if number in self._numbers  else -1 for number in numbers]


# fmt: on

if __name__ == "__main__":
    week8 = LotteryNumbers(8, [1, 2, 3, 10, 20, 30, 33])
    my_numbers = [1, 4, 7, 10, 11, 20, 30]

    print(week8.hits_in_place(my_numbers))
