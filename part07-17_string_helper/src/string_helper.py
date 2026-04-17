# Write your solution here
import string
def change_case(string : str):
    newString = ""
    for char in string:
        if char == char.upper():
            newString += char.lower()
        else:
            newString += char.upper()
    return newString

def split_in_half(string : str):
    halfLen = len(string) // 2
    
    return string[:halfLen], string[halfLen:]

def remove_special_characters(orig_word : str):
    new_word = orig_word
    for char in orig_word:
        if char in string.ascii_letters or char in string.digits or char in string.whitespace:
            continue
        else:
            new_word = new_word.replace(char,"")
    return new_word

if __name__ == "__main__":
    print("Using Import")