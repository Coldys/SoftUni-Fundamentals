product = {}

while True:
    command = input()
    if command == 'buy':
        break

    command = command.split(' ')
    if command[0] not in product:
        product.update({command[0]: {
            'price': float(command[1]),
            'quantity': int(command[2])
        }})
    else:
        new_qty = product[command[0]]['quantity'] + int(command[2])

        product[command[0]] = {
            'price': float(command[1]),
            'quantity': new_qty
        }

for key, value in product.items():
    print(f"{key} -> {value['price'] * value['quantity']:.2f}")
