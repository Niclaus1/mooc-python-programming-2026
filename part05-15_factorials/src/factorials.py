# Write your solution here
def factorials(n : int):
    dict = {}
    value = 1
    
    for x in range(1,n + 1):

        value = value * (x)
        dict[x] = value
        
    return dict


if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
    