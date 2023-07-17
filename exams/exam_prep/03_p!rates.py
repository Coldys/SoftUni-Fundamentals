cities = {}

while True:
    user_input = input().split('||')

    if user_input[0] == 'Sail':
        break

    if user_input[0] in cities:
        cities[user_input[0]][0] += int(user_input[1])
        cities[user_input[0]][1] += int(user_input[2])
    else:
        people = int(user_input[1])
        gold = int(user_input[2])
        cities[user_input[0]] = [people, gold]


def plunder(data, town, people, gold):
    if data[town][0] < people:
        people = data[town][0]

    if data[town][1] < gold:
        gold = data[town][1]

    data[town][0] -= people
    data[town][1] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

    if data[town][0] <= 0 or data[town][1] <= 0:
        del data[town]
        print(f"{town} has been wiped off the map!")
    return data


def prosper(data, town, gold):
    data[town][1] += gold
    print(f"{gold} gold added to the city treasury. {town} now has {data[town][1]} gold.")
    return data


while True:
    command = input().split('=>')

    if command[0] == 'End':
        break
    elif command[0] == 'Plunder':
        cities = plunder(cities, command[1], int(command[2]), int(command[3]))
    elif command[0] == 'Prosper':
        if int(command[2]) < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities = prosper(cities, command[1], int(command[2]))

if len(cities) > 0:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city in cities:
        print(f'{city} -> Population: {cities[city][0]} citizens, Gold: {cities[city][1]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
