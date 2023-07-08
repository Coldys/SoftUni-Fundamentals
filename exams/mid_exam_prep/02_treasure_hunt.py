def main():
    treasure_box = input().split('|')

    while True:
        command = input()
        if command == 'Yohoho!':
            break

        command = command.split(' ')

        if command[0] == 'Loot':
            treasure_box = loot(treasure_box, command[1:])
        elif command[0] == 'Drop':
            treasure_box = drop(treasure_box, int(command[1]))
        elif command[0] == 'Steal':
            treasure_box = steal(treasure_box, int(command[1]))

    if len(treasure_box) <= 0:
        return "Failed treasure hunt."

    gain = 0
    for item in treasure_box:
        gain += len(item)

    avg_gain = round(gain / len(treasure_box), 2)

    return f"Average treasure gain: {avg_gain:.2f} pirate credits."


def loot(treasure, items):
    for item in items:
        if item not in treasure:
            treasure.insert(0, item)

    return treasure


def drop(treasure, idx: int):
    if idx in range(len(treasure)):
        item = treasure.pop(idx)
        treasure.append(item)

    return treasure


def steal(treasure, items_num: int):
    if items_num >= len(treasure):
        print(', '.join(treasure))
        return []
    else:
        print(', '.join(treasure[len(treasure) - items_num:]))
        return treasure[:len(treasure) - items_num]


if __name__ == "__main__":
    print(main())
