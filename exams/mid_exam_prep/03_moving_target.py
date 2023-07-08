def shoot(targets, idx: int, power: int):
    if idx in range(len(targets)):
        targets[idx] -= power
        if targets[idx] <= 0:
            targets.pop(idx)

    return targets


def add(targets, idx: int, value: int):
    if idx in range(len(targets)):
        targets.insert(idx, value)
    else:
        print("Invalid placement!")
    return targets


def strike(targets, idx: int, radius: int):
    upper_bound = idx + radius
    lower_bound = idx - radius

    if upper_bound in range(len(targets)) and lower_bound in range(len(targets)):
        targets = targets[:lower_bound] + targets[upper_bound + 1:]
    else:
        print("Strike missed!")

    return targets


main_targets = [int(x) for x in input().split(' ')]

while True:

    command = input()

    if command == 'End':
        break

    command = command.split(' ')
    if command[0] == 'Shoot':
        main_targets = shoot(main_targets, int(command[1]), int(command[2]))
    elif command[0] == 'Add':
        main_targets = add(main_targets, int(command[1]), int(command[2]))
    elif command[0] == 'Strike':
        main_targets = strike(main_targets, int(command[1]), int(command[2]))

main_targets = [str(x) for x in main_targets]
print('|'.join(main_targets))
