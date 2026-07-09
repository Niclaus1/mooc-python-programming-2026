# Write your solution here
def prime_numbers():

    number = 2
    while True:
        is_prime = True
        for num in range(2, int(number**0.5) + 1):
            if number % num == 0:
                is_prime = False
                break

        if is_prime:
            yield number
        number += 1


if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))
