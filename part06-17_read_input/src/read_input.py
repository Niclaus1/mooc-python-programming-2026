# Write your solution here
def read_input(userInput:str,minValue:int,maxValue:int):
    
    while True:
        try:
            userInput = input(userInput)
            number = int(userInput)
            if number > minValue and number < maxValue:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {minValue} and {maxValue}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 1,5)
    print("You typed in:", number)
