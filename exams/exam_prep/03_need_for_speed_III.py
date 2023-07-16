n = int(input())

cars = {}
for _ in range(n):
    key, milage, fuel = input().split('|')
    if int(fuel) > 75:
        fuel = 75
    cars[key] = [int(milage), int(fuel)]


def drive(data, car, distance, fuel_needed):
    if data[car][1] >= fuel_needed:
        data[car][0] += distance
        data[car][1] -= fuel_needed
        print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
    else:
        print("Not enough fuel to make that ride")

    if data[car][0] > 100000:
        del data[car]
        print(f"Time to sell the {car}!")
    return data


def refuel(data, car, fuel):
    can_take = 75 - data[car][1]
    if can_take > 0:
        if can_take >= fuel:
            can_take = fuel

    data[car][1] += can_take
    print(f"{car} refueled with {can_take} liters")
    return data


def revert(data, car, miles):
    if data[car][0] - miles < 10000:
        data[car][0] = 10000
    else:
        data[car][0] -= miles
        print(f"{car} mileage decreased by {miles} kilometers")
    return data


while True:
    command = input().split(' : ')

    if command[0] == 'Stop':
        break
    elif command[0] == 'Drive':
        cars = drive(cars, command[1], int(command[2]), int(command[3]))
    elif command[0] == 'Refuel':
        cars = refuel(cars, command[1], int(command[2]))
    elif command[0] == 'Revert':
        cars = revert(cars, command[1], int(command[2]))

for c in cars:
    print(f"{c} -> Mileage: {cars[c][0]} kms, Fuel in the tank: {cars[c][1]} lt.")