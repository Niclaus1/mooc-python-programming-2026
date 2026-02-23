# Write your solution here

def add(dict : dict,name: str, number : str):
    phoneBook = dict
    phoneBook[name] = number
    return phoneBook

def contact():
    phoneBook = {}
    
    while True:
        userInput = input("1 search, 2 add, 3 quit:")
        
        if userInput == "1":
            inputName = input("name: ")
            if inputName in phoneBook:
                for number in phoneBook[inputName]:
                    print(number)
            else:
                print("no number")
                
        elif userInput == "2":
            
            inputName = input("name: ")
            inputNumber = input("number: ")
            if inputName not in phoneBook:
                add(phoneBook, inputName, [])
                
            phoneBook[inputName].append(inputNumber)
            
            print("ok!")
        elif userInput == "3":
            print("quitting...")
            break
contact()