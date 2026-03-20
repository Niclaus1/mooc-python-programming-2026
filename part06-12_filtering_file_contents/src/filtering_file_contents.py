# Write your solution here
def filter_solutions():
    fileCorrect = "correct.csv"
    fileIncorrect = "incorrect.csv"
    fileName = "solutions.csv"
    correct_list = []
    incorrect_list = []

    with open(fileName) as new_file:
        for line in new_file:
            line = line.strip()
            parts = line.split(";")

            if "-" in parts[1]:
                nums = parts[1].split("-")
                res = int(nums[0]) - int(nums[1])

            elif "+" in parts[1]:
                nums = parts[1].split("+")
                res = int(nums[0]) + int(nums[1])

            if res == int(parts[2]):
                correct_list.append(line)
            else:
                incorrect_list.append(line)

    addSolution(fileCorrect, correct_list)
    addSolution(fileIncorrect, incorrect_list)


def addSolution(filename: str, solution: list):
    with open(filename, "w") as write_file:
        for sol in solution:
            write_file.write(f"{sol}\n")


if __name__ == "__main__":
    filter_solutions()
