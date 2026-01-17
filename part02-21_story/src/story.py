# Write your solution here
string = ""
last_word = ""
while True:
    word = input('Please type in a word:')
    
    if word == 'end' or word == last_word:
        print(string)
        break
    
    string = string + word + ' '   
    last_word = word
    