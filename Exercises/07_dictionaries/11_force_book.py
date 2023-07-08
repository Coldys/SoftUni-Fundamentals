def add_user(data, side, name):
    skip = False

    for k, v in data.items():
        if name in v:
            skip = True
            break
    if not skip:
        if side in user_data:
            user_data[side].append(name)
        else:
            user_data[side] = [name]
    return data


def change_side(data, name, new_side):
    person_exists = False
    current_key = ''
    for k, v in data.items():
        if name in v:
            person_exists = True
            current_key = k
            break

    if person_exists:
        data[current_key].remove(name)
        if len(user_data[current_key]) <= 0:
            user_data.pop(current_key)

    if new_side in user_data:
        user_data[new_side].append(name)
        print(f"{name} joins the {new_side} side!")
    else:
        user_data[new_side] = [name]
        print(f"{name} joins the {new_side} side!")

    return data


user_data = {}

while True:
    command = input()

    if command == 'Lumpawaroo':
        break

    if ' | ' in command:
        command = command.split(' | ')
        user_data = add_user(user_data, command[0], command[1])

    elif ' -> ' in command:
        command = command.split(' -> ')
        user_data = change_side(user_data, command[0], command[1])

for key, value in user_data.items():
    print(f'Side: {key}, Members: {len(value)}')
    for member in value:
        print(f'! {member}')
