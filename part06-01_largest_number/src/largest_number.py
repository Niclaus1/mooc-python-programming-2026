# write your solution here
def largest():
    with open('src/numbers.txt') as new_file:
        largest_number = 0
        
        for line in new_file:
            line = int(line.replace("\n", ""))

            if largest_number < line:
                largest_number = line

    return largest_number

if __name__ == "__main__":
    print(largest())