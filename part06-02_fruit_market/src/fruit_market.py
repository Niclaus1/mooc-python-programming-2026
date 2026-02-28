# write your solution here
def read_fruits():

    with open("fruits.csv") as new_file:
        fruit_dict = {}
        
        for line in new_file:
            line = line.replace("\n", "")
            fruits = line.split(';')
            
            fruit = fruits[0]
            price = float(fruits[1])
            
            fruit_dict[fruit] = price
            
    return fruit_dict

if __name__ == "__main__":
    print(read_fruits())