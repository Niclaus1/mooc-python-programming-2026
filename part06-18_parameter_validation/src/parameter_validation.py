# Write your solution here
def new_person(name:str, age:int):    
    wordsLen = name.split()
    print(len(wordsLen))
    if name != "" and len(name) < 40 and age > 0 and age < 150 and len(wordsLen) > 1:
        return (name,age)
    else:
        raise ValueError

if __name__ == "__main__":
    print(new_person("Sirkka-Liisa Virtanen-Aftenbladet-Totterstrom-Lahtiska-Vanamo-Kullervoinen", 32))