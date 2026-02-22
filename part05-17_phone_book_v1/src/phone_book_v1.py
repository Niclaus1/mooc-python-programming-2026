# Write your solution here
def search(dict : dict,name : str):
    phoneBook = dict
    if name not in phoneBook:
        return "no number"
    return phoneBook[name]

def add(dict : dict,name: str, number : str):
    phoneBook = dict
    phoneBook[name] = number
    return phoneBook

def contact():
    phoneBook = {}
    
    while True:
        userInput = input("1 search, 2 add, 3 quit: ")
        
        if userInput == "1":
            inputName = input("name: ")
            print(search(phoneBook,inputName))

        elif userInput == "2":
            inputName = input("name: ")
            inputNumber = input("number: ")
            add(phoneBook, inputName, inputNumber)
            print("ok!")

        else:
            print("quitting...")
            break
contact()