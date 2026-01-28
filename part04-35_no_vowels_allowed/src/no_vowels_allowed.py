# Write your solution here
def no_vowels(word : str):
    vowels = ['a','e','i','o','u']

    string = word
    for vowel in vowels:
        string = string.replace(vowel, "")
    
    return string
if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))