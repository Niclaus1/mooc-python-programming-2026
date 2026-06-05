# WRITE YOUR SOLUTION HERE:


class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year
        self._value = int(str(self._year) + str(self._month) + str(self._day))

        if self._day > 31:
            months_added = self._day // 31
            self._month = months_added - 12
            if months_added > 12:
                year_added = months_added // 12
                self._year += year_added

    def __str__(self):
        return f"{self._day}.{self._month}.{self._year}"

    def __lt__(self, other):
        return self._value < other._value

    def __gt__(self, other):
        print(self._value, other._value)
        return self._value > other._value

    def __eq__(self, other):
        return self._value == other._value

    def __ne__(self, other):
        return self._value != other._value

    def __add__(self, other):
        days_added = self._day + other
        months_added = self._month
        years_added = self._year

        while days_added > 30:
            days_added -= 30
            months_added += 1
            if months_added > 12:
                months_added = 1
                years_added += 1

        add_date = SimpleDate(days_added, months_added, years_added)

        return add_date

    def __sub__(self, other):
        self_days = self._day + (self._month * 30) + (self._year * 360)
        other_days = other._day + (other._month * 30) + (other._year * 360)
        return abs(self_days - other_days)


if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2 - d1)
    print(d1 - d2)
    print(d1 - d3)
