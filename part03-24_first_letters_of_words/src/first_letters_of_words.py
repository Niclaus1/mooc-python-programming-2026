# Write your solution here
word = input('Please type in a sentence:')
word_len = len(word)

step = 0
print(word[0])  

while step < word_len:
    
    if word[step] == ' ' and (step + 1 < word_len):
        print(word[step + 1])
    step += 1