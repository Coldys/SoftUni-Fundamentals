n = int(input())
plants = {}
for _ in range(n):
    plant_data = input().split('<->')
    plants[plant_data[0]] = [plant_data[1], []]


def rate(data, plant, rating):
    data[plant][1].append(rating)
    return data


def update(data, plant, rarity):
    data[plant][0] = rarity
    return data


def reset(data, plant):
    data[plant][1] = []
    return data


while True:

    command = input().split(': ')

    if command[0] == 'Exhibition':
        break
    elif command[0] == 'Rate':
        command = command[1].split(' - ')
        if command[0] in plants:
            plants = rate(plants, command[0], int(command[1]))
        else:
            print('error')
    elif command[0] == 'Update':
        command = command[1].split(' - ')
        if command[0] in plants:
            plants = update(plants, command[0], command[1])
        else:
            print('error')
    elif command[0] == 'Reset':
        if command[1] in plants:
            plants = reset(plants, command[1])
        else:
            print('error')

print('Plants for the exhibition:')
for key in plants:
    if len(plants[key][1]) > 0:
        rating = sum(plants[key][1])/len(plants[key][1])
    else:
        rating = 0.0
    print(f'- {key}; Rarity: {plants[key][0]}; Rating: {rating:.2f}')
