# Write your solution here
import string


def run(program):
    ram = {}
    result = []

    label = {}
    place = 0
    for i in program:
        if ":" in i:
            label[i.replace(":", "")] = place
        place += 1
    print(label)

    counter = 0
    while counter < len(program):
        instruction = program[counter]
        parts = instruction.split()

        cmd = parts[0]

        dest = parts[1] if len(parts) > 1 else 0
        if dest not in ram:
            ram[dest] = 0

        src = 0
        if len(parts) > 2:
            val = parts[2]
            if val in string.ascii_uppercase:
                src = ram.get(val, 0)
            else:
                try:
                    src = int(val)
                except ValueError:
                    src = 0

        match cmd:
            case "END":
                break
            case "PRINT":
                if parts[1] in string.ascii_letters:
                    result.append(ram.get(dest, 0))
                else:
                    result.append(int(parts[1]))
            case "MOV":
                ram[dest] = src
            case "ADD":
                ram[dest] += src
            case "SUB":
                ram[dest] -= src
            case "MUL":
                ram[dest] *= src
            case "JUMP":
                counter = label[parts[1]]
                continue
            case "IF":
                a = ram.get(parts[1], 0)
                cmp = parts[2]
                src = parts[3]
                jmp = parts[5]

                b = 0
                if src in string.ascii_uppercase:
                    b = ram.get(src, 0)
                else:
                    try:
                        b = int(src)
                    except ValueError:
                        b = 0

                print(a, cmp, b)
                if cmp == ">" and a > b:
                    counter = label[jmp]
                elif cmp == "!=" and a != b:
                    counter = label[jmp]
                elif cmp == "==" and a == b:
                    counter = label[jmp]
                elif cmp == "<" and a < b:
                    counter = label[jmp]
                elif cmp == "<=" and a <= b:
                    counter = label[jmp]
                elif cmp == ">" and a > b:
                    counter = label[jmp]
                elif cmp == ">=" and a >= b:
                    counter = label[jmp]
                else:
                    counter += 1
                    continue
        counter += 1
    return result


if __name__ == "__main__":
    program3 = [
        "MOV N 100",
        "PRINT 2",
        "MOV A 3",
        "start:",
        "MOV B 2",
        "MOV Z 0",
        "test:",
        "MOV C B",
        "new:",
        "IF C == A JUMP virhe",
        "IF C > A JUMP pass_by",
        "ADD C B",
        "JUMP new",
        "virhe:",
        "MOV Z 1",
        "JUMP pass_by2",
        "pass_by:",
        "ADD B 1",
        "IF B < A JUMP test",
        "pass_by2:",
        "IF Z == 1 JUMP pass_by3",
        "PRINT A",
        "pass_by3:",
        "ADD A 1",
        "IF A <= N JUMP start",
    ]
    result = run(program3)
    print(result)
