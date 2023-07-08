msg = input()


def move(text: str, idx: int):
    text = text[idx:] + text[:idx]
    return text


def insert(text: str, idx: int, symbol: str):
    text = text[:idx] + symbol + text[idx:]
    return text


def change_all(text: str, sub_str: str, replacement_str: str):
    text = text.replace(sub_str, replacement_str)
    return text


while True:
    command = input().split('|')

    if command[0] == 'Decode':
        break
    elif command[0] == 'Move':
        msg = move(msg, int(command[1]))
    elif command[0] == 'Insert':
        msg = insert(msg, int(command[1]), command[2])
    elif command[0] == 'ChangeAll':
        msg = change_all(msg, command[1], command[2])

print(f'The decrypted message is: {msg}')
