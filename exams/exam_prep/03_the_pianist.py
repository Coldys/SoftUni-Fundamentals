def add(data, piece: str, composer: str, key: str):
    if piece not in data:
        data[piece] = {'key': key,  'composer': composer}
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")
    return data


def remove(data, piece):
    if piece in data:
        del data[piece]
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return data


def change_key(data, piece: str, new_key: str):
    if piece in data:
        data[piece]['key'] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return data


n = int(input())
user_data = {}

for i in range(n):
    user_input = input().split('|')
    if user_input[0] not in user_data:
        user_data[user_input[0]] = {'key': user_input[2],  'composer': user_input[1]}

while True:
    command = input().split('|')

    if command[0] == 'Stop':
        break

    elif command[0] == 'Add':
        user_data = add(user_data, command[1], command[2], command[3])

    elif command[0] == 'Remove':
        user_data = remove(user_data, command[1])

    elif command[0] == 'ChangeKey':
        user_data = change_key(user_data, command[1], command[2])

for key in user_data:
    print(f"{key} -> Composer: {user_data[key]['composer']}, Key: {user_data[key]['key']}")
