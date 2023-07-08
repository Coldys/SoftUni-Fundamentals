def  insert_space(text: str, idx: int):
    text = text[:idx] + ' ' + text[idx:]
    print(text)
    return text


def reverse(text: str, sub_str: str):
    idx = text.find(sub_str)
    if idx > -1:
        text = text[:idx] + text[idx + len(sub_str):]
        text += sub_str[::-1]
        print(text)
    else:
        print('error')
    return text


def change_all(text: str, old_str: str, new_str: str):
    text = text.replace(old_str, new_str)
    print(text)
    return text


msg = input()

while True:
    command = input().split(':|:')

    if command[0] == 'Reveal':
        break

    elif command[0] == 'InsertSpace':
        msg = insert_space(msg, int(command[1]))

    elif command[0] == 'Reverse':
        msg = reverse(msg, command[1])

    elif command[0] == 'ChangeAll':
        msg = change_all(msg, command[1], command[2])


print(f'You have a new text message: {msg}')
