# Write your solution here
def dict_of_numbers():
    numbers = {}
    
    format = {
        0 : 'zero',      1 : 'one',
        2 : 'two',       3 : 'three',
        4 : 'four',      5 : 'five',
        6 : 'six',       7 : 'seven',
        8 : 'eight',     9 : 'nine',
        10 : 'ten',      11 : 'eleven',
        12 : 'twelve',   13 : 'thirteen',
        14 : 'fourteen', 15 : 'fifteen',
        16 : 'sixteen',  17 : 'seventeen',
        18 : 'eighteen', 19 : 'nineteen',
        20 : 'twenty',   30 : 'thirty',
        40 : 'forty',   50 : 'fifty',
        60 : 'sixty',    70 : 'seventy',
        80 : 'eighty',   90 : 'ninety',
    }
    
    for number in range(100):

        if number >= 0 and number <= 20:
            numbers[number] = format[number]
                    
        elif number > 20 and number < 30:
            numbers[number] = f'{format[20]}-{format[number - 20]}'
    
        elif number > 30 and number < 40:
            numbers[number] = f'{format[30]}-{format[number - 30]}'
            
        elif number > 40 and number < 50:
            numbers[number] = f'{format[40]}-{format[number - 40]}'
            
        elif number > 50 and number < 60:
            numbers[number] = f'{format[50]}-{format[number - 50]}'
            
        elif number > 60 and number < 70:
            numbers[number] = f'{format[60]}-{format[number - 60]}'
            
        elif number > 70 and number < 80:
            numbers[number] = f'{format[70]}-{format[number - 70]}'
            
        elif number > 80 and number < 90:
            numbers[number] = f'{format[80]}-{format[number - 80]}'
            
        elif number > 90 and number <= 99:
            numbers[number] = f'{format[90]}-{format[number - 90]}'
        else:
            numbers[number] = format[number]
    return numbers


if __name__ == "__main__":
    numbers = dict_of_numbers()

    print(numbers[0])
