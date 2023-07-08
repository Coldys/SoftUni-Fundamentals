products = input().split(' ')

while True:
    command = input()

    if command == 'No Money':
        break

    user_data = command.split(' ')
    if user_data[0] == 'OutOfStock':
        products = [x if x != user_data[1] else "None" for x in products]
    elif user_data[0] == 'Required':
        idx = int(user_data[2])
        if 0 <= idx <= len(products):
            products[idx] = user_data[1]
    elif user_data[0] == 'JustInCase':
        products[-1] = user_data[1]

products = [x for x in products if x != 'None']

print(' '.join(products))
