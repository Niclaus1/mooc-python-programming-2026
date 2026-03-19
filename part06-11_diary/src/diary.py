# Write your solution here
while True:
    filename = "diary.txt"
    print("1 - add an entry, 2 - read entries, 0 - quit")
    userInput = input("Function: ")

    match userInput:
        case "1":
            entry = input("Dairy entry: ")
            with open(filename,"a") as new_file:
                new_file.write(f'{entry}\n')
            print("Diary saved")
        case "2":
            print("Entries: ")
            with open(filename) as new_file:
                for line in new_file:
                    print(line.strip())

        case "0":
            print("Bye now!")
            break