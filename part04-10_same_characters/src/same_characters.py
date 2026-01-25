# Write your solution here
def same_chars(string: str, a: int, b: int):
    
    if len(string) - 1 < a or len(string) - 1 < b:
        return False
    else:
        return string[a] == string[b]
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("programmer", 6, 7))
    print(same_chars("programmer", 0, 4))
    print(same_chars("abc", 0, 3))