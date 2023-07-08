companies = {}

while True:
    command = input().split(' -> ')

    if command[0] == 'End':
        break

    if command[0] not in companies:
        companies[command[0]] = [command[1]]
    else:
        if command[1] not in companies[command[0]]:
            companies[command[0]].append(command[1])

for key, value in companies.items():
    print(key)
    for id_number in value:
        print(f'-- {id_number}')
