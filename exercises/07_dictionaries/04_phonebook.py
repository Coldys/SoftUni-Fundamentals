phonebook = {}
n = None
while True:
    user_input = input()
    user_input = user_input.split('-')

    if len(user_input) == 1:
        n = int(user_input[0])
        break

    phonebook[user_input[0]] = user_input[1]

for _ in range(n):
    name = input()

    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')
