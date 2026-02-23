# Write your solution here
def invert(dictionary: dict):
    keys = []
    values = []

    for key, value in dictionary.items():
        keys.append(value)
        values.append(key)

    dictionary.clear()

    for index in range(len(keys)):
        dictionary[keys[index]] = values[index]
    

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)

