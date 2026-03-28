# Write your solution here
def filter_incorrect():
    correctList = []
    with open('lottery_numbers.csv') as file:
        for line in file:
            lineStrip = line.strip()
            lineFormat = lineStrip.replace(" ",',').replace(";",",")
            parts = lineFormat.split(',')

            if len(parts) == 9 and parts[1].isnumeric() :
                match = True
                for element in parts[2:]:   
                    if element.isnumeric() and int(element) < 40 and int(element) > 0 and parts[2:].count(element) == 1:
                        continue
                    else:
                        match = False
                        break
                if match and line not in correctList:
                    correctList.append(line)

    with open("correct_numbers.csv", 'w') as new_file:
        for data in correctList:
            new_file.write(data)

if __name__ == "__main__":
    filter_incorrect()