def balanced_brackets(my_string: str):
    clean_list = "".join([char for char in my_string if char in "()[]"])
    pairs = {"(": ")", "[": "]"}

    if len(clean_list) == 0:
        return True

    if clean_list[0] not in pairs or clean_list[-1] not in pairs.values():
        return False

    if pairs[clean_list[0]] == clean_list[-1]:
        return balanced_brackets(clean_list[1:-1])
    else:
        return False


if __name__ == "__main__":
    ok = balanced_brackets("(()]")
    print(ok)
