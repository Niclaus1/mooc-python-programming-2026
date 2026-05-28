# WRITE YOUR SOLUTION HERE:
class ListHelper:
    def __init__(self):
        pass

    @classmethod
    def greatest_frequency(cls, my_list: list):
        most_common = my_list[0]

        for item in my_list:
            if my_list.count(item) > my_list.count(most_common):
                most_common = item
        return most_common

    @classmethod
    def doubles(cls, my_list: list):
        twice_appeared = []

        for item in my_list:
            if my_list.count(item) > 1 and item not in twice_appeared:
                twice_appeared.append(item)
        return len(twice_appeared)


if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
