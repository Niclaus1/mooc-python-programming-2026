# Write your solution here
def shortest(list : list):
    shortest_string = list[0]

    for word in list:
        if len(word) < len(shortest_string):
            shortest_string = word

    return shortest_string

if __name__ == "__main__":
        
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)