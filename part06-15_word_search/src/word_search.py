# Write your solution here
def find_words(search_term: str):
    search_term = search_term.lower().strip()
    with open('words.txt') as new_file:
        wordList = []
        for line in new_file:
            line = line.strip()

            if "*" in search_term:
                wildcard = search_term.replace("*", "")
                if search_term.index('*') == 0 and line.endswith(wildcard):
                    wordList.append(line)
                elif search_term.index('*') != 0 and line.startswith(wildcard):
                    wordList.append(line)
    
            elif '.' in search_term:
                if len(search_term) == len(line):
                    match = True
                    for i in range(len(search_term)):
                        if search_term[i] != '.' and search_term[i] != line[i]:
                            match = False
                            break
                    if match: wordList.append(line)
            elif "." not in search_term and "*" not in search_term:
                wordList.append(search_term)
                break
    return(wordList)


if __name__ == "__main__":
    print(find_words(input("Type a word: ")))




