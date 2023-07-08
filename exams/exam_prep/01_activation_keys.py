def contains(key: str, sub_str: str):
    if key.find(sub_str) > -1:
        return f'{key} contains {sub_str}'
    return f'Substring not found!'


def flip(key, flip_type: str, str_idx: int, end_idx: int):
    if flip_type == 'Upper':
        key = key[:str_idx] + key[str_idx:end_idx].upper() + key[end_idx:]
    elif flip_type == 'Lower':
        key = key[:str_idx] + key[str_idx:end_idx].lower() + key[end_idx:]

    print(key)
    return key


def slice_key(key, str_idx: int, end_idx: int):
    key = key[:str_idx] + key[end_idx:]
    print(key)
    return key


raw_key = input()

while True:
    command = input().split('>>>')

    if command[0] == 'Generate':
        break

    elif command[0] == 'Contains':
        print(contains(raw_key, command[1]))

    elif command[0] == 'Flip':
        raw_key = flip(raw_key, command[1], int(command[2]), int(command[3]))

    elif command[0] == 'Slice':
        raw_key = slice_key(raw_key, int(command[1]), int(command[2]))

print(f'Your activation key is: {raw_key}')
