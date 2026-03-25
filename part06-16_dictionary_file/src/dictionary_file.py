# Write your solution here
def add(filename : str, words : str) -> str:
    with open (filename, 'a') as new_file:
        new_file.write(words)
    print("Dictionary entry added")

def search(filename : str, find : str):
    with open(filename) as new_file:

        for line in new_file:
            parts = line.strip().split("-")
            if find in parts[0] or find in parts[1]:
                print(f'{parts[0]}-{parts[1]}')
        
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    userInput = input("Function: ")
    
    match userInput:
        case "1":
            wordFin = input("The word in Finnish: ").strip()
            wordEng = input("The word in Enginer: ").strip()
            add("dictionary.txt",f'{wordFin} - {wordEng}\n')
        case "2":
            term = input("Search term: ").strip()
            search("dictionary.txt",term)
        case "3":
            print("Bye!")
            break