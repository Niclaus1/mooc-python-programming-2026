# Write your solution here
def no_shouting (list : list):
    lowered_list = []
    
    for word in list:
        if word.isupper():
            continue
        else:
            lowered_list.append(word)


    return lowered_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)