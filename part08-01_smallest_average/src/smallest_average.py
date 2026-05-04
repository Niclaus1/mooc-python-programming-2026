# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    person1Avg = (person1["result1"] + person1["result2"] + person1["result3"]) / 2
    person2Avg = (person2["result1"] + person2["result2"] + person2["result3"]) / 2
    person3Avg = (person3["result1"] + person3["result2"] + person3["result3"]) / 2

    if person1Avg < person2Avg and person1Avg < person3Avg:
        return person1
    elif person2Avg < person1Avg and person2Avg < person3Avg:
        return person2
    elif person3Avg < person1Avg and person3Avg < person2Avg:
        return person3
    else:
        return "Its all a Tie"


if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))
