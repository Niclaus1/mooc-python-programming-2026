# Write your solution here
import difflib 
wordtxt = "wordlist.txt"

wordlists = []
with open(wordtxt) as new_file:
    for line in new_file:
        # parts = line.split()
        wordlists.append(line.strip())

user_Input = input('Write text: ')
words = user_Input.split(" ")
sentence = ""
incorrect_words = []

for word in words:
    if word.lower() in wordlists:
        sentence += f' {word}'
    else:
        sentence += f' *{word}*'
        incorrect_words.append(word)
        
print(sentence)
if sentence != "":
    print("suggestions: ")
    for word in incorrect_words:
        
        suggest_list = difflib.get_close_matches(word,wordlists)
        print(f'{word}: {", ".join(suggest_list)}')
    