# Write your solution here
temperature = int(input('Please tyoe in a temperature (F):'))

celsius = (temperature - 32) / 1.8

if celsius < 0:
    print(f'{temperature} degrees Fahrenheit equals {celsius} degrees Celsius')
    print("Brr! It's cold in here!")
else:
    print(f'{temperature} degrees Fahrenheit equals {celsius} degrees Celsius')
