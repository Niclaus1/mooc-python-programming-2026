# Write your solution here
print('What is the weather forecast for tomorrow?')
temperature = int(input('Temperature:'))
rain_status = input('Will it rain (yes/no):')

message = 'Wear jeans and a T-shirt \n'
if temperature <= 20:
    message += 'I recommend a jumper as well \n'
if temperature <= 10:
    message += 'Take a jacket with you \n'
if temperature <= 5:
    message += 'Make it a warm coat, actually \nI think gloves are in order \n'
if rain_status == 'yes':
    message += "Don't forget your umbrella!"
    
print(message)