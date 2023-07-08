password = input()


def take_odd(text: str):
    new_text = ''
    for i in range(1, len(text), 2):
        new_text += text[i]
    print(new_text)
    return new_text


def cut(text: str, idx: int, length: int):
    sub_str = text[idx:idx + length]
    text = text.replace(sub_str, "", 1)
    print(text)
    return text


def substitute(text: str, sub_str: str, replacement: str):
    if sub_str in text:
        text = text.replace(sub_str, replacement)
        print(text)
    else:
        print("Nothing to replace!")
    return text


while True:
    command = input().split(' ')
    if command[0] == 'Done':
        break
    elif command[0] == 'TakeOdd':
        password = take_odd(password)
    elif command[0] == 'Cut':
        password = cut(password, int(command[1]), int(command[2]))
    elif command[0] == 'Substitute':
        password = substitute(password, command[1], command[2])

print(f"Your password is: {password}")
