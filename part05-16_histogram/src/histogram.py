# Write your solution here

def histogram(word : str):
    dict = {}
    star = "*"

    for char in word:
        if char not in dict:
            dict[char] = ""
        dict[char] = dict[char] + star

    for key, value in dict.items():
        print(f'{key} {value}')

if __name__ == "__main__":
    histogram("abba")


