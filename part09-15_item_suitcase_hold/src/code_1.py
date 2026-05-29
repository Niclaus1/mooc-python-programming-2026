# Write your solution here:
class Item:
    def __init__(self, book_name: str, book_weight: int):
        self._name = book_name
        self._weight = book_weight

    def name(self):
        return self._name

    def weight(self):
        return self._weight

    def __str__(self):
        return f"{self._name} ({self._weight} kg)"


class Suitcase:
    def __init__(self, max_weight: int):
        self._max_weight = max_weight
        self._current_weight = 0
        self.item_list: list = []

    def add_item(self, item: Item):
        if item.weight() + self._current_weight <= self._max_weight:
            self._current_weight += item.weight()
            self.item_list.append(item)

    def __str__(self):
        item_count = len(self.item_list)

        if item_count == 1:
            return f"{len(self.item_list)} item ({self._current_weight} kg)"
        else:
            return f"{len(self.item_list)} items ({self._current_weight} kg)"

    def print_items(self):
        for item in self.item_list:
            print(item)

    def weight(self):
        return self._current_weight

    def heaviest_item(self):
        curr_item = self.item_list[0]

        for item in self.item_list:
            if item.weight() > curr_item.weight():
                curr_item = item
        return curr_item


class CargoHold:
    def __init__(self, max_weight: int):
        self._weight = max_weight
        self.cargo_list: list = []

    def add_suitcase(self, suitcase: Suitcase):
        if (self._weight - suitcase.weight()) >= 0:
            self.cargo_list.append(suitcase)
            self._weight -= suitcase.weight()

    def __str__(self):
        item_count = len(self.cargo_list)
        if item_count == 1:
            return f"{len(self.cargo_list)} suitcase, space for {self._weight} kg"
        else:
            return f"{len(self.cargo_list)} suitcases, space for {self._weight} kg"

    def print_items(self):
        for suitcase in self.cargo_list:
            suitcase.print_items()


if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
