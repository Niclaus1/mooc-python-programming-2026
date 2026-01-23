# Write your solution here
def print_many_times(word, count):
    step = 0
    while step < count:
        print(word)
        step += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)