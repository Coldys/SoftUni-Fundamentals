is_on = True
output = ""
while is_on:
    command = input()

    if command.lower() == "end":
        is_on = False
        break
    elif command == "SoftUni":
        continue

    for i in range(len(command)):
        output += command[i] * 2

    print(output)
    output = ""