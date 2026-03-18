# write your solution here
wordlist = "wordlist.txt"

wordlists = []
with open(wordlist) as new_file:
    for line in new_file:
        # parts = line.split()
        wordlists.append(line.strip())


user_Input = input('Write text: ')
words = user_Input.split(" ")
sentence = ""

for word in words:
    if word.lower() in wordlists:
        sentence += f' {word}'
    else:
        sentence += f' *{word}*'
print(sentence)