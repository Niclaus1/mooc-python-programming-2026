# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents / 100
        self._value = self._euros + self._cents

    def __str__(self):
        return f"{self._euros + self._cents:.2f} eur"

    def __eq__(self, another):
        return self._value == another._value

    def __lt__(self, other):
        return self._value < other._value

    def __gt__(self, other):
        return self._value > other._value

    def __ne__(self, other):
        return self._value != other._value

    def __add__(self, other):
        return f"{(self._value + other._value):.2f} eur"

    def __sub__(self, other):
        if (self._value - other._value) < 0:
            raise ValueError("a negative result is not allowed")
        return f"{(self._value - other._value):.2f} eur"


if __name__ == "__main__":
    money1 = Money(1, 0)
    money2 = Money(1, 0)

    a = money1 + money2
    print(a)
