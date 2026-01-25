# Write your solution here
def squared (string, number):

    row = 0
    
    index = 0
    while row < number:
        col = 0 
        
        while col < number:
            print(string[index], end= "")
            
            index += 1
            
            if index >= len(string):
                index = 0
            col += 1
        print()
        
        row += 1

if __name__ == "__main__":
    squared('niclaus' , 3)