resources = {}
while True:
    resource = input()

    if resource == 'stop':
        break

    amount = int(input())

    resources[resource] = resources.get(resource, 0) + amount

for key, value in resources.items():
    print(f'{key} -> {value}')
