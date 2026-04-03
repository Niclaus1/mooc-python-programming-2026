# Write your solution here
import json

def print_persons(filename : str):
    with open(filename) as file:
        data = file.read()

        names = json.loads(data)
        for name in names:
            print(f"{name['name']} {name['age']} years ({', '.join(name['hobbies'])})")
if __name__ == "__main__":
    print_persons('file1.json')